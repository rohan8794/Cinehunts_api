from flask import Flask, jsonify, Response  # Import Response
from flask_cors import CORS
from pymongo import MongoClient
from bson import json_util  # Import json_util from bson
import json

app = Flask(__name__)
CORS(app)

# MongoDB connection
client = MongoClient("mongodb+srv://orgdriphy:ttkCwzgb3yqCdAXN@cluster0.soas0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['Testing']
collection = db['Movies']

@app.route('/api/movies', methods=['GET'])
def get_movies():
    # Retrieve movies sorted by newest first, including title and image URL
    movies_cursor = collection.find({}, {'_id': 1, 'title': 1, 'image': 1}).sort("_id", -1)  # Sort by latest added
    movies_list = list(movies_cursor)  # Convert cursor to list

    # Use json_util to serialize the data
    return Response(json.dumps(movies_list, default=json_util.default), mimetype='application/json')

# Health check endpoint for Koyeb deployment
@app.route('/health', methods=['GET'])
def health_check():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
