import os, json, base64
from dotenv import load_dotenv
from firebase_admin import credentials, initialize_app, firestore
from flask import Flask, jsonify
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

encoded_json = os.getenv("FIREBASE_CREDENTIALS")
if not encoded_json:
    raise Exception("FIREBASE_CREDENTIALS not found in environment")

decoded_json = base64.b64decode(encoded_json).decode('utf-8')
service_account_info = json.loads(decoded_json)
cred = credentials.Certificate(service_account_info)
initialize_app(cred)

db = firestore.client()

@app.route('/api/data')
def get_data():
    docs = db.collection('your_collection_name').stream()
    return jsonify([doc.to_dict() for doc in docs])

if __name__ == '__main__':
    app.run(debug=True)
