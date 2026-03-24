# 🎙️ Multilingual TTS Python

> Projeto em Python que traduz um texto para múltiplos idiomas e gera áudio automaticamente (Text-to-Speech).

---

## 🚀 Funcionalidades

✔ Tradução automática de texto  
✔ Suporte a múltiplos idiomas (Inglês 🇺🇸 e Espanhol 🇪🇸)  
✔ Geração de áudio (.mp3)  
✔ Reprodução automática dos áudios  

---

## 🧠 Tecnologias utilizadas

- Python 3  
- gTTS (Google Text-to-Speech)  
- deep-translator  

---

## 📦 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/multilingual-tts-python.git
cd multilingual-tts-python
```

### 2. Crie um ambiente virtual
```bash
python -m venv .venv
```

### 3. Ative o ambiente virtual

**Windows:**
```powershell
.venv\Scripts\activate
```

### 4. Instale as dependências
```bash
pip install -r requirements.txt
```

---

## ▶️ Como usar

```bash
python main.py
```

---

## 💡 Exemplo de uso

### Entrada:
```
Olá eu sou o Theo e estou gerando áudios no python
```

### Saída:
- Tradução em inglês
- Tradução em espanhol
- Geração dos arquivos:
  - `audio_en.mp3`
  - `audio_es.mp3`

---

## 📁 Estrutura do projeto

```bash
multilingual-tts-python/
├── main.py            # Arquivo principal
└── README.md          # Documentação
```

---

## ⚠️ Observações

- É necessário conexão com a internet  
- A reprodução automática funciona no Windows com:

```python
os.system("start arquivo.mp3")
```

---

## 👨‍💻 Autor

**Theo**

---

## 📌 Licença

Este projeto é livre para estudos e uso pessoal.
