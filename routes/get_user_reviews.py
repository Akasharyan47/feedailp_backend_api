from flask import Blueprint, request, jsonify
from firebase_admin import firestore
import re

get_user_reviews_bp = Blueprint('get_user_reviews_bp', __name__)
db = firestore.client()

def sanitize_email(email: str) -> str:
    return re.sub(r'[^\w]', '_', email.lower())  # Same function as in submit API

@get_user_reviews_bp.route('/api/user_reviews', methods=['GET'])
def get_reviews_by_email():
    try:
        email = request.args.get('email')
        if not email:
            return jsonify({"error": "Email query param is required"}), 400

        email_doc_id = sanitize_email(email)

        # Path: reviews/{sanitized_email}/products/
        reviews_ref = db.collection("reviews").document(email_doc_id).collection("products")
        docs = reviews_ref.stream()

        reviews = []
        for doc in docs:
            data = doc.to_dict()
            data['product_id'] = doc.id  # Add product ID from document
            reviews.append(data)

        return jsonify({
            "status": "success",
            "email": email,
            "review_count": len(reviews),
            "reviews": reviews
        }), 200

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
