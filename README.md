# PrivacyLens 🔍

PrivacyLens is an AI-powered web application that simplifies privacy policies into clear, concise summaries. It features audio support, risk analysis, multi-language translation, and an AI chatbot to help users better understand privacy policies.

## 🌟 Features

- **Quick Summary**: Convert lengthy privacy policies into easy-to-understand summaries
- **Risk Analysis**: Identify potential privacy risks in policies
- **Audio Support**: Listen to summaries through text-to-speech conversion
- **Multi-Language Support**: Translate summaries into different languages
- **AI Chat Assistant**: Get instant answers to your privacy policy questions

## 🚀 Technologies Used

### Backend Framework
- **Backend**: Flask
- **Frontend**: HTML, CSS (Tailwind CSS), JavaScript, React

### AI/ML Models
- **Summarization**: Pre-trained T5 transformer model and tokenizer for text summarization
- **Sentiment Analysis**: Pre-trained BERT-based model for privacy policy grading
- **Chatbot**: LangChain with Ollama (LLama 3.2)

### Additional Technologies
- **Text-to-Speech**: gTTS (Google Text-to-Speech)
- **Styling**: Tailwind CSS

## 📋 Prerequisites

- Python 3.8 or higher
- Ollama installed and running
- Modern web browser

## 🛠️ Installation

1. Clone the repository:
```bash
git clone [https://github.com/lemonn0902/privacy-policy-summary-app.git](https://github.com/lemonn0902/privacy-policy-summary-app.git)
cd privacy-policy-summary-app
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Make sure Ollama is running with LLama 3.2 model:
```bash
ollama run llama3.2
```

5. The T5 and BERT models will be downloaded automatically on first run

6. Start the Flask application:
```bash
python app.py
```

7. Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## 📁 Project Structure

```
privacy-policy-summary-app/
├── app.py                 # Main Flask application
├── sum.py                 # Summarization functions (T5 model)
├── sentiment.py           # Sentiment analysis functions (BERT model)
├── static/
│   ├── mp3/              # Generated audio files
│   └── css/              # Custom CSS files
├── templates/
│   ├── index.html        # Home page
│   ├── about.html        # About page
│   ├── try-it.html       # Summarizer page
│   ├── translate.html    # Translation page
│   └── chat.html         # Chat interface
└── requirements.txt       # Python dependencies
```

## 🔧 Configuration

The application uses the following default configuration:
- Host: 127.0.0.1
- Port: 5000
- Debug Mode: Enabled

To modify these settings, edit the `app.run()` parameters in `app.py`.


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- Shreya Srivastava - ([lemonn0902)](https://github.com/lemonn0902)

## 📞 Support

For support, email shreya.srivastava0902@gmail.com or create an issue in the GitHub repository.
