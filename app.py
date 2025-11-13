import os
import re
import nltk
from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def preprocessar_texto(texto):
    padroes_remover = [
        r"\b(ol[áa]|oi|bom dia|boa tarde|boa noite|tudo bem|como vai)\b",
        r"\b(atenciosamente|grato|agradeço|obrigad[ao]|obg|valeu|abraços|abs)\b",
        r"enviado de meu celular",
        r"--+.*",            
        r"^>.*$",            
        r"^from:.*$",        
        r"^to:.*$",
        r"^subject:.*$",
    ]

    for padrao in padroes_remover:
        texto = re.sub(padrao, "", texto, flags=re.MULTILINE | re.IGNORECASE)

    texto = re.sub(r"http\S+|www\S+|@\S+|[^a-zA-ZÀ-ÿ\s]", "", texto)
    texto = texto.lower()

    palavras = nltk.word_tokenize(texto, language='portuguese')

    stop_words = set(stopwords.words('portuguese'))
    palavras = [p for p in palavras if p not in stop_words]

    lemmatizer = WordNetLemmatizer()
    palavras = [lemmatizer.lemmatize(p) for p in palavras]

    return " ".join(palavras)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/processar', methods=['POST'])
def processar_email():
    texto_input = request.form.get('texto', '').strip()
    arquivo_input = request.files.get('arquivo')
    
    has_text = bool(texto_input)
    has_file = arquivo_input and arquivo_input.filename != ''

    if has_text and has_file:
        return jsonify({
            'categoria': 'Erro de Input', 
            'resposta_sugerida': 'Por favor, envie APENAS o texto ou APENAS o arquivo, não ambos.'
        }), 400 

    if not has_text and not has_file:
        return jsonify({
            'categoria': 'Erro de Input', 
            'resposta_sugerida': 'Nenhum texto ou arquivo enviado.'
        }), 400 

    texto_email = ""

    if 'texto' in request.form:
        texto_email = request.form['texto']

    if 'arquivo' in request.files:
        arquivo = request.files['arquivo']
        caminho = os.path.join(UPLOAD_FOLDER, arquivo.filename)
        arquivo.save(caminho)
        if arquivo.filename.endswith('.txt'):
            with open(caminho, 'r', encoding='utf-8') as f:
                texto_email = f.read()

    if not texto_email.strip():
        return jsonify({'categoria': 'Improdutivo', 'resposta_sugerida': 'Nenhum texto enviado.'})

    texto_email_limpo = preprocessar_texto(texto_email)

    prompt = f"""
Classifique o seguinte email em **uma das categorias**: Produtivo ou Improdutivo.

**Categorias de Classificação**
- Produtivo: Emails que requerem uma ação ou resposta específica 
    (ex.: solicitações de suporte técnico, atualização sobre casos em aberto, dúvidas sobre o sistema).
- Improdutivo: Emails que não necessitam de uma ação imediata 
    (ex.: mensagens de felicitações, agradecimentos).

Retorne **somente uma linha com a categoria** (Produtivo ou Improdutivo).
Em seguida, gere **uma resposta automática direta ao email**, adequada à categoria.

Formato de saída esperado:
<Produtivo ou Improdutivo>
<Mensagem de resposta curta>

Email (pré-processado):
{texto_email_limpo}
"""

    try:
        resp = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[{"parts": [{"text": prompt}]}]
        )
        resposta_texto = resp.candidates[0].content.parts[0].text.strip()

        linhas = resposta_texto.split("\n")
        categoria = linhas[0] if linhas else "Produtivo"
        resposta_sugerida = "\n".join(linhas[1:]) if len(linhas) > 1 else "Obrigado pelo contato."

        return jsonify({'categoria': categoria, 'resposta_sugerida': resposta_sugerida})

    except Exception as e:
        print("Erro Gemini:", e)
        return jsonify({'categoria': 'Erro', 'resposta_sugerida': 'Não foi possível processar o email.'})


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=10000, debug=True)
