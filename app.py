from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
from sum import summarize_text, text_to_speech  # Import both functions from sum.py
import os
import traceback
from gtts import gTTS


# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Directory to save the MP3 files
MP3_DIR = 'static/mp3'
os.makedirs(MP3_DIR, exist_ok=True)

# Route to serve the HTML form
@app.route('/')
def index():
    return render_template('index.html')  # Serve the HTML file from templates folder

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

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)  # Run on localhost with the specified port
