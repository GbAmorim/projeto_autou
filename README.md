📧 Classificador de Emails com Gemini AI (Flask)

Este projeto é uma aplicação web simples construída com Flask (Python) e Gemini API que realiza a triagem automática de emails, classificando-os como "Produtivos" (requerem ação) ou "Improdutivos" (apenas informativos), e sugerindo uma resposta automática.

💻 Tecnologias Utilizadas

Categoria

Tecnologia

Uso

Backend

Python (Flask, Gunicorn)

Servidor web, rotas, lógica de pré-processamento.

Inteligência Artificial

Google Gemini API (gemini-2.5-flash)

Classificação de emails e geração de respostas automáticas.

Pré-processamento

NLTK

Tokenização (ToktokTokenizer), remoção de Stop Words e Lematização para Português.

Configuração

python-dotenv

Gerenciamento seguro da chave da API via arquivo .env.

Frontend

HTML5, CSS, JavaScript

Estrutura da interface, estilização e lógica de submissão assíncrona (fetch).

Estrutura do Projeto

A estrutura do projeto está organizada da seguinte forma, refletindo os arquivos de código e assets:

PROJETO_AUTOU/
├── static/                   # Arquivos estáticos do Frontend
│   ├── email-illustration.svg 
│   ├── logo-autou.webp
│   ├── night.svg             # Ícone de tema escuro
│   ├── script.js             # Lógica do frontend (fetch, manipulação do DOM)
│   ├── style.css             # Estilos CSS (incluindo responsividade e tema)
│   └── sun.svg               # Ícone de tema claro
├── templates/
│   └── index.html            # Estrutura HTML da interface 
├── uploads/                  # Diretório temporário para arquivos .txt enviados
│   ├── gmail.txt             # (Exemplo)
│   └── mensagem.txt          # (Exemplo)
├── venv/                     # Ambiente virtual Python (ignorado pelo Git)
├── .env.example              # Modelo para o arquivo .env (chave da API)
├── .gitignore                # Regras de arquivos ignorados (venv, .env, uploads/)
├── app.py                    # Lógica principal do Flask e pré-processamento
├── Procfile                  # Configuração para deploy em serviços como Render ou Railway
└── requirements.txt          # Lista de dependências Python (Flask, google-genai, nltk, etc.)


Pré-requisitos

Para rodar este projeto, você precisará de:

Python 3.8+

Uma Chave da API do Google Gemini.

🚀 Como Executar Localmente

Siga estas etapas para configurar e executar o projeto em sua máquina.

1. Clonar o Repositório

git clone <URL_DO_SEU_REPOSITORIO>
cd PROJETO_AUTOU


2. Configurar o Ambiente Virtual (Recomendado)

É crucial isolar as dependências do projeto.

# Cria o ambiente virtual
python -m venv venv

# Ativa o ambiente virtual
# No Linux/macOS:
source venv/bin/activate
# No Windows (PowerShell):
.\venv\Scripts\Activate


3. Instalar Dependências

Com o ambiente virtual ativado, instale as bibliotecas necessárias listadas no requirements.txt:

pip install -r requirements.txt


4. Configurar a Chave da API

Crie um arquivo chamado .env na raiz do projeto (na mesma pasta de app.py).

Atenção: O arquivo .gitignore garante que este arquivo NÃO será enviado ao GitHub, protegendo sua chave secreta.

Use o .env.example como base e preencha sua chave:

# Conteúdo do arquivo .env:
GEMINI_API_KEY="SUA_CHAVE_AQUI"


5. Executar o Aplicativo Flask

O projeto foi configurado para ser executado via Gunicorn, o que simula melhor o ambiente de produção:

# Se o gunicorn não estiver instalado, instale-o (já está no requirements.txt)
# pip install gunicorn 

# Inicia o servidor Gunicorn
gunicorn app:app -b 127.0.0.1:5000


6. Acessar a Interface

Abra seu navegador e acesse:

http://127.0.0.1:5000/

Você pode testar a classificação colando o conteúdo de um email de exemplo diretamente na caixa de texto.

🛠️ Detalhes da Implementação

Pré-Processamento (NLTK)

O módulo app.py realiza:

Downloads de NLTK: Garante o download de stopwords e wordnet no início, essencial para a portabilidade em ambientes de nuvem.

Tokenização Robusta: Utiliza o ToktokTokenizer para tokenização em Português, que é mais estável em comparação com o método padrão que depende de pacotes estatísticos.

Limpeza: Remove cabeçalhos, saudações, URLs e aplica lematização.

Classificação (Gemini)

A função processar_email envia o email pré-processado ao modelo gemini-2.5-flash com um prompt específico, solicitando:

A classificação em uma única linha (Produtivo ou Improdutivo).

Uma mensagem de resposta sugerida logo abaixo.

O frontend então exibe ambas as saídas.

Desenvolvido com Python (Flask), NLTK, HTML/CSS/JS e Google Gemini API.
