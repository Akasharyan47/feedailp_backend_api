from flask import Blueprint, jsonify
from firebase_admin import firestore

get_reviews_bp = Blueprint('get_reviews', __name__)
db = firestore.client()

@get_reviews_bp.route('/get_reviews', methods=['GET'])
def get_reviews():
    try:
        docs = db.collection('reviews').stream()
        reviews = []
        for doc in docs:
            data = doc.to_dict()
            reviews.append(data)
        return jsonify({"status": "success", "data": reviews}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
