from flask import Blueprint, jsonify, request
from firebase_admin import firestore

get_user_reviews_bp = Blueprint('get_user_reviews', __name__)
db = firestore.client()

@get_user_reviews_bp.route('/get_user_reviews/<user_id>', methods=['GET'])
def get_user_reviews(user_id):
    try:
        docs = db.collection('reviews').where('user_id', '==', user_id).stream()
        reviews = [doc.to_dict() for doc in docs]
        return jsonify({"status": "success", "data": reviews}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
