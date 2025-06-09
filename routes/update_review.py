from flask import Blueprint, request, jsonify
from firebase_admin import firestore

update_review_bp = Blueprint('update_review', __name__)
db = firestore.client()

@update_review_bp.route('/update_review/<review_id>', methods=['PUT'])
def update_review(review_id):
    try:
        data = request.get_json()
        review_ref = db.collection('reviews').document(review_id)
        review_ref.update(data)
        return jsonify({"status": "success", "message": "Review updated successfully!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
