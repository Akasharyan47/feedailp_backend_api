# routes/update_review.py
from flask import Blueprint, request, jsonify
from firebase_admin import firestore, auth

update_review_bp = Blueprint('update_review_bp', __name__, url_prefix='/api')

db = firestore.client()

@update_review_bp.route('/update_review', methods=['POST'])
def update_review():
    try:
        data = request.get_json()
        review_id = data.get("id")
        uid = data.get("uid")

        if not review_id or not uid:
            return jsonify({"status": "error", "message": "Missing review ID or user UID"}), 400

        # Ensure user owns the review (you can extend this with Firestore rules or a secure query)
        doc_ref = db.collection('reviews').document(review_id)
        existing_doc = doc_ref.get()
        if not existing_doc.exists:
            return jsonify({"status": "error", "message": "Review not found"}), 404

        review_data = existing_doc.to_dict()
        if review_data.get("uid") != uid:
            return jsonify({"status": "error", "message": "Unauthorized"}), 403

        # Update Firestore document
        update_fields = {
            "user": data.get("user"),
            "rating": data.get("rating"),
            "comment": data.get("comment"),
            "date": data.get("date"),
            "company": data.get("company"),
            "product": data.get("product"),
            "service_experience": data.get("service_experience")
        }
        doc_ref.update(update_fields)

        return jsonify({"status": "success", "message": "Review updated successfully"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
