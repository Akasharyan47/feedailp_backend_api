from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore
import os
import base64
import json
from dotenv import load_dotenv

# Load environment
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Decode Firebase Base64 key and initialize app
firebase_base64_key = os.getenv("FIREBASE_BASE64_KEY")
firebase_key_dict = json.loads(base64.b64decode(firebase_base64_key).decode("utf-8"))

if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_key_dict)
    firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()

# POST API to store review
@app.route('/api/submit_review', methods=['POST'])
def submit_review():
    try:
        data = request.get_json()

        required_fields = ['product', 'District', 'Star_Ratings', 'Yes_No']
        for field in required_fields:
            if field not in data:
                return jsonify({"status": "error", "message": f"Missing field: {field}"}), 400

        db.collection("reviews").add(data)

        return jsonify({"status": "success", "message": "Review submitted successfully"}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
