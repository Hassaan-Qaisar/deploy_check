# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re
from dbConnection import tweets 

app = Flask(__name__)
CORS(app)
analyzer = SentimentIntensityAnalyzer()

def preprocess_tweet(tweet):
    # Remove mentions
    tweet = re.sub(r'@[A-Za-z0-9_]+', '', tweet)
    # Remove HTTP links
    tweet = re.sub(r'http\S+', '', tweet)
    return tweet

@app.route('/api/net_sentiment', methods=['GET'])
def sentiment_analysis():
    positive_threshold = 0.05
    negative_threshold = -0.05
    
    positive_count = 0
    negative_count = 0
    neutral_count = 0
    
    for sentence in tweets:
        preprocessed_sentence = preprocess_tweet(sentence)
        vs = analyzer.polarity_scores(preprocessed_sentence)
        compound_score = vs['compound']
        pos_score = vs['pos']
        neg_score = vs['neg']
        
        if (compound_score > positive_threshold) and (pos_score > 0.2):
            positive_count += 1
        elif compound_score < negative_threshold:
            negative_count += 1
        else:
            neutral_count += 1
    
    result = {
        "positive": positive_count,
        "negative": negative_count,
        "neutral": neutral_count
    }
    
    return jsonify(result)

@app.route('/api/batch_sentiment', methods=['POST'])
def batch_sentiment_analysis():
    positive_threshold = 0.05
    negative_threshold = -0.05
    data = request.json  # Get JSON data from request
    sentiment_labels = []
    
    for tweet in data:
        preprocessed_tweet = preprocess_tweet(tweet)
        vs = analyzer.polarity_scores(preprocessed_tweet)
        compound_score = vs['compound']
        pos_score = vs['pos']
        
        if (compound_score > positive_threshold) and (pos_score > 0.2):
            sentiment_labels.append("Positive")
        elif compound_score < negative_threshold:
            sentiment_labels.append("Negative")
        else:
            sentiment_labels.append("Neutral")
    
    return jsonify(sentiment_labels)

@app.route('/', methods=['GET'])
def home():
    return "Homepage"
    
if __name__ == "__main__":
    app.run() 