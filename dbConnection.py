import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get MongoDB URI from environment variable
mongodb_uri = os.getenv("MONGODB_URI")

client = MongoClient(mongodb_uri)

# client = MongoClient('mongodb+srv://hassaanqaisar2:8BhDrTI7uKnKhjsL@cluster0.1fxixvl.mongodb.net/?retryWrites=true&w=majority')

db = client['Psl_data']
collection = db['tweets']

# only fetch tweets which contain psl7 hashtag
documents = collection.find({"hashtags": "psl7"})

# Loading data from first 50 documents
tweets = []
for i, doc in enumerate(documents):
    if i == 4000:
        break
    tweets.append(doc['tweet'])

# Print the length of the 'tweets' array
# print(f"Number of tweets: {len(tweets)}")