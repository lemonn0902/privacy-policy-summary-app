

from transformers import pipeline

# Load pre-trained BERT-based sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def analyze_sentiment(text):
    """Analyze sentiment of a given text section using BERT."""
    result = sentiment_pipeline(text[:512])[0]  # BERT can only process 512 tokens at once
    return result["label"], result["score"]  # Returns sentiment label and confidence score

def split_text(text, max_length=500):
    """Split long text into smaller sections to fit within BERT's token limit."""
    words = text.split()
    return [" ".join(words[i:i + max_length]) for i in range(0, len(words), max_length)]

def calculate_risk_score(summary):
    """Analyze sentiment of each section and calculate the total risk score."""
    sections = split_text(summary)
    total_score = 0

    for section in sections:
        sentiment, confidence = analyze_sentiment(section)

        if sentiment.lower() == "positive":
            total_score += 2  # Positive sentiment means safer policy
        elif sentiment.lower() == "negative":
            total_score -= 3  # Negative sentiment means risky policy

    return total_score

def assign_risk_grade(score):
    """Assign a risk grade based on the total risk score."""
    if score >= 5:
        return "A (Very Low Risk)"
    elif score >= 2:
        return "B (Low Risk)"
    elif score >= -1:
        return "C (Medium Risk)"
    elif score >= -5:
        return "D (High Risk)"
    else:
        return "E (Very High Risk)"

def analyze_privacy_policy(summary):
    """Full pipeline: analyze summary, calculate risk score, and assign a grade."""
    risk_score = calculate_risk_score(summary)
    risk_grade = assign_risk_grade(risk_score)
    return risk_grade, risk_score


