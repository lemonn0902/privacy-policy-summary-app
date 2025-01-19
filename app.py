from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
from sum import summarize_text, text_to_speech  # Import functions from sum.py
import os
import traceback
from gtts import gTTS
from sentiment import analyze_privacy_policy
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Directory to save the MP3 files
MP3_DIR = 'static/mp3'
os.makedirs(MP3_DIR, exist_ok=True)

model = OllamaLLM(model="llama3.2")

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model
context = ""


# Route to render the chat page
@app.route('/chat')
def chat_page():
    return render_template('chat.html')

# API endpoint for chatbot conversation
@app.route('/chat', methods=['POST'])
def chat():
    global context
    user_input = request.json.get('question')  # Get the user input from the POST request
    
    if not user_input:
        return jsonify({"error": "No question provided"}), 400

    # Use the chain to get the AI response
    result = chain.invoke({"context": context, "question": user_input})
    
    # Update context for future questions
    context += f"\nUser: {user_input}\nAI: {result}"

    return jsonify({"response": result})


# Route to home page 
@app.route('/')
def home():
    return render_template('index.html')

#Route for try it page
@app.route('/try-it')
def try_it():
    return render_template('try-it.html')

# Route for About Us page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for Translate page
@app.route('/translate')
def translate():
    return render_template('translate.html')


# Define route for summarization
@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        # Get privacy policy from the request
        data = request.json
        privacy_policy = data.get('privacy_policy', '')

        if not privacy_policy:
            return jsonify({"error": "Privacy policy text is required"}), 400

        # Call the summarize_text function to summarize the policy
        summary = summarize_text(privacy_policy)

        # Generate speech from summary
        tts = gTTS(summary, lang='en')
        mp3_filename = 'summary.mp3'
        mp3_filepath = os.path.join(MP3_DIR, mp3_filename)
        tts.save(mp3_filepath)

        # Return MP3 URL and summary
        mp3_url = f"/static/mp3/{mp3_filename}"
        return jsonify({"summary": summary, "audio_url": mp3_url})

    except Exception as e:
        # Log the full error details to terminal for debugging
        print(f"Error: {str(e)}")
        print("Full traceback:", traceback.format_exc())
        return jsonify({"error": "An unexpected error occurred."}), 500

# Route to serve the MP3 file
@app.route('/static/mp3/<filename>')
def serve_mp3(filename):
    return send_from_directory(MP3_DIR, filename)

# Route for grading the summary using sentiment analysis
@app.route('/grade', methods=['POST'])
def grade():
    try:
        # Get summary text from the request
        data = request.json
        summary = data.get('summary', '')

        if not summary:
            return jsonify({"error": "Summary text is required"}), 400

        # Call the analyze_privacy_policy function from sentiment.py to calculate the grade and score
        grade, score = analyze_privacy_policy(summary)

        
        return jsonify({"grade": grade, "score": score})

    except Exception as e:
        # Log the full error details to terminal for debugging
        print(f"Error: {str(e)}")
        print("Full traceback:", traceback.format_exc())
        return jsonify({"error": "An unexpected error occurred."}), 500





if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)  # Run on localhost with the specified port
