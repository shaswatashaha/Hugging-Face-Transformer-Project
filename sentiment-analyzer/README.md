# 🧠 Sentiment Analyzer using Hugging Face Transformers

This project is a lightweight **Sentiment Analysis Web App** built using [Hugging Face Transformers](https://huggingface.co/transformers/) and [Gradio](https://gradio.app/). It allows users to input a text and receive a real-time classification of the sentiment as **Positive** or **Negative**, along with a confidence score.

---

## 🚀 Features

- 🧪 Uses a pretrained Hugging Face model: `distilbert-base-uncased-finetuned-sst-2-english`
- 🎨 Custom-styled Gradio interface with color-coded results and emojis
- ⚡ Instant output for real-time sentiment detection
- 🧠 Hugging Face pipeline abstracts the model backend (no explicit PyTorch or TensorFlow code)

---

## 🛠️ Tech Stack

- **Python**
- **Transformers (Hugging Face)**
- **Gradio** (for UI)

---

## 📦 Installation

### Clone the repository:
```bash
git clone https://github.com/yourusername/huggingface-projects.git
cd huggingface-projects/sentiment-analyzer






# README.md
# 🤗 Hugging Face Sentiment Analyzer

This is a simple web app that uses `distilbert-base-uncased-finetuned-sst-2-english` from Hugging Face to analyze sentiment in user-inputted text.

## 🚀 Demo
Real-time sentiment analysis using Hugging Face Transformers and Gradio.

## 🧠 Features
- Uses Hugging Face `pipeline` API
- Custom HTML-styled sentiment output
- Emoji and color-coded result display
- Clean, themed Gradio interface

## 📦 Requirements
```bash
pip install -r requirements.txt
```

## ▶️ Run the app
```bash
python app.py
```

## 📸 Screenshot
Include a `screenshot.png` of your app's UI for better visual appeal.

## 👨‍💼 Why this project?
- Demonstrates practical use of Transformers
- Shows understanding of inference, UI, and theming
- Great for ML portfolios and job interviews

# requirements.txt
transformers
torch
gradio
