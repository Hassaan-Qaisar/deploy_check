# Sentiment Analysis Flask Server

This project is a Flask-based sentiment analysis server that analyzes the sentiment of text input using VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool. It provides two endpoints: one for analyzing a text inputs from db and another for analyzing multiple text inputs in batch.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/Hassaan-Qaisar/sentiment_server
   ```

2. Navigate to the project directory:
   ```
   cd sentiment-analysis-flask
   ```

3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the MongoDB URI:
   - Create a `.env` file in the project directory.
   - Add your MongoDB URI in the `.env` file:
     ```
     MONGODB_URI=your-mongodb-uri
     ```

5. Start the Flask server:
   ```
   python app.py
   ```

6. Once the server is running, you can access the endpoints at the following URLs:
   - Single text analysis: [http://localhost:5000/api/net_sentiment](http://localhost:5000/api/net_sentiment)
   - Batch text analysis: [http://localhost:5000/api/batch_sentiment](http://localhost:5000/api/batch_sentiment)

## Endpoints

### Analyze Single Text
- **URL:** `/api/net_sentiment`
- **Method:** GET
- **Description:** Analyzes the sentiment of a text inputs from database.
- **Example:** [http://localhost:5000/api/net_sentiment](http://localhost:5000/api/net_sentiment)

### Analyze Batch Text
- **URL:** `/api/batch_sentiment`
- **Method:** POST
- **Description:** Analyzes the sentiment of multiple text inputs provided in a JSON array.
- **Example:** [http://localhost:5000/api/batch_sentiment](http://localhost:5000/api/batch_sentiment)

## Technologies Used

- Flask
- VADER Sentiment Analysis
- MongoDB
- Python-Dotenv
- Flask-CORS
