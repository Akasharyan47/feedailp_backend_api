from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
import base64
import json
import firebase_admin
from firebase_admin import credentials, firestore

# Setup
load_dotenv()
app = Flask(__name__)
CORS(app)

# Firebase Init
encoded_json = os.getenv("FIREBASE_CREDENTIALS")
missing_padding = len(encoded_json) % 4
if missing_padding != 0:
    encoded_json += '=' * (4 - missing_padding)

decoded_json = base64.b64decode(encoded_json).decode('utf-8')
service_account_info = json.loads(decoded_json)
cred = credentials.Certificate(service_account_info)
firebase_admin.initialize_app(cred)
db = firestore.client()

# Register Routes
from routes.submit_review import submit_review_bp
from routes.get_reviews import get_reviews_bp
from routes.get_user_reviews import get_user_reviews_bp
from routes.update_review import update_review_bp
from routes.service_types import service_types_bp

app.register_blueprint(submit_review_bp)
app.register_blueprint(get_reviews_bp)
app.register_blueprint(get_user_reviews_bp)
app.register_blueprint(update_review_bp)
app.register_blueprint(service_types_bp)

@app.route('/', methods=['GET'])
def health_check():
    return {"message": "Feedailp API is running"}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
