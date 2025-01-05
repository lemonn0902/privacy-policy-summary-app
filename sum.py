from transformers import T5Tokenizer, T5ForConditionalGeneration
from gtts import gTTS
import os

# Load pre-trained T5 model and tokenizer
model = T5ForConditionalGeneration.from_pretrained("t5-base")
tokenizer = T5Tokenizer.from_pretrained("t5-base")

# Function to split text into chunks
def split_text(text, max_length=512):
    # Tokenize text
    tokens = tokenizer.encode(text, return_tensors="pt", truncation=False)
    num_tokens = tokens.shape[1]
    
    # Split tokens into chunks
    chunks = [tokens[:, i:i+max_length] for i in range(0, num_tokens, max_length)]
    
    return chunks

# Function to summarize each chunk
def summarize_text(text):
    chunks = split_text(text)
    summaries = []

    for chunk in chunks:
        # Decode the chunk
        chunk_text = tokenizer.decode(chunk[0], skip_special_tokens=True)

        input_text = f"Provide a clear summary focusing on how personal data is handled, including cookies, consent, and user responsibilities: {chunk_text}"
        
        # Prepare the input for summarization
        input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

        # Generate summary
        summary_ids = model.generate(input_ids, max_length=150, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        summaries.append(summary)

    return ' '.join(summaries)

# Function to convert text to speech using gTTS
def text_to_speech(text, filename="summary.mp3"):
    tts = gTTS(text, lang='en')  # You can change the language if needed
    tts.save(filename)          # Save the speech as an MP3 file
