# 📧 Classificador de Emails com Gemini AI (Flask)

Este projeto é uma aplicação web simples construída com **Flask (Python)** e **Gemini API** que realiza a triagem automática de emails, classificando-os como **"Produtivos"** (requerem ação) ou **"Improdutivos"** (apenas informativos), e sugerindo uma resposta automática.

---

## 💻 Tecnologias Utilizadas

| Categoria               | Tecnologia                           | Uso                                                                               |
| ----------------------- | ------------------------------------ | --------------------------------------------------------------------------------- |
| Backend                 | Python (Flask, Gunicorn)             | Servidor web, rotas, lógica de pré-processamento                                  |
| Inteligência Artificial | Google Gemini API (gemini-2.5-flash) | Classificação de emails e geração de respostas automáticas                        |
| Pré-processamento       | NLTK                                 | Tokenização (ToktokTokenizer), remoção de Stop Words e Lematização para Português |
| Configuração            | python-dotenv                        | Gerenciamento seguro da chave da API via arquivo `.env`                           |
| Frontend                | HTML5, CSS, JavaScript               | Estrutura da interface, estilização e lógica de submissão assíncrona (fetch)      |

---

## 🗂 Estrutura do Projeto

```
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
```

---

## Pré-requisitos

Para rodar este projeto, você precisará de:

* Python 3.8+
* Uma chave da **API do Google Gemini**

---

## 🚀 Como Executar Localmente

Siga estas etapas para configurar e executar o projeto em sua máquina:

### 1. Clonar o Repositório

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd PROJETO_AUTOU
```

### 2. Configurar o Ambiente Virtual (Recomendado)

```bash
# Cria o ambiente virtual
python -m venv venv

# Ativa o ambiente virtual
# No Linux/macOS:
source venv/bin/activate
# No Windows (PowerShell):
.\venv\Scripts\Activate
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar a Chave da API

Crie um arquivo chamado `.env` na raiz do projeto (mesma pasta de `app.py`) usando como base o `.env.example`:

```env
GEMINI_API_KEY="SUA_CHAVE_AQUI"
```

> ⚠️ O arquivo `.env` é ignorado pelo Git para proteger sua chave secreta.

### 5. Executar o Aplicativo Flask

O projeto foi configurado para ser executado via Gunicorn, simulando um ambiente de produção:

```bash
# Se o gunicorn não estiver instalado, instale-o (já está no requirements.txt)
# pip install gunicorn

# Inicia o servidor Gunicorn
gunicorn app:app -b 127.0.0.1:5000
```

### 6. Acessar a Interface

Abra o navegador e acesse:

```
http://127.0.0.1:5000/
```

Você pode testar a classificação colando o conteúdo de um email ou enviando um arquivo `.txt`.

---

## 🛠️ Detalhes da Implementação

### Pré-Processamento (NLTK)

* **Downloads automáticos**: garante que `stopwords` e `wordnet` sejam baixados em qualquer ambiente.
* **Tokenização**: utiliza o `ToktokTokenizer` para português.
* **Limpeza**: remove cabeçalhos, saudações, URLs e aplica lematização.
* **Stopwords**: palavras comuns em português são removidas para melhorar a análise.

### Classificação (Gemini)

* O modelo `gemini-2.5-flash` recebe o email pré-processado e retorna:

  * **Categoria**: `Produtivo` ou `Improdutivo`
  * **Resposta sugerida**: mensagem curta para responder ao email
* A interface exibe automaticamente a categoria e a resposta.

---

## 🔧 Tecnologias e Bibliotecas

* Python 3.8+
* Flask
* NLTK
* python-dotenv
* google-genai
* Gunicorn (para produção)
* HTML, CSS, JavaScript (frontend)

---

## 📂 Observações

* O diretório `uploads/` é temporário e usado apenas para arquivos `.txt` enviados.
* O arquivo `.env` não deve ser enviado para repositórios públicos.
* Adaptável para deploy em Render, Railway ou Heroku via `Procfile`.
