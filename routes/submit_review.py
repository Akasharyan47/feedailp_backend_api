from flask import Blueprint, jsonify, request
from firebase_admin import firestore
import re

submit_review_bp = Blueprint('submit_review_bp', __name__)
db = firestore.client()

def sanitize_email(email: str) -> str:
    return re.sub(r'[^\w]', '_', email.lower())  # email ke special chars replace karo

@submit_review_bp.route('/api/submit_review', methods=['POST'])
def submit_review():
    try:
        data = request.get_json()

        required_fields = ['product', 'District', 'Star_Ratings', 'Yes_No', 'email', 'name', 'reviewText']
        for field in required_fields:
            if field not in data or data[field] in [None, '', [], {}]:
                return jsonify({
                    "status": "error",
                    "message": f"Missing or empty field: {field}"
                }), 400

        product_info = data['product']
        try:
            product_id = product_info['product']['product_id']
        except Exception as e:
            return jsonify({
                "status": "error",
                "message": f"Invalid product structure: {str(e)}"
            }), 400

        # 📌 Sanitize email to make it Firestore safe
        email_doc_id = sanitize_email(data['email'])

        # 📦 Prepare data
        review_data = {
            "product": product_info,
            "District": data['District'],
            "Star_Ratings": data['Star_Ratings'],
            "Yes_No": data['Yes_No'],
            "email": data['email'],
            "name": data['name'],
            "reviewText": data['reviewText'],
            "timestamp": firestore.SERVER_TIMESTAMP
        }

        # 🧠 Save data: reviews -> email_doc_id -> products -> product_id -> data
        db.collection("reviews") \
            .document(email_doc_id) \
            .collection("products") \
            .document(product_id) \
            .set(review_data)

        print(f"✅ Data saved for email: {email_doc_id}, product: {product_id}")
        return jsonify({
            "status": "success",
            "message": f"Review saved under {email_doc_id}/{product_id}",
            "email_doc_id": email_doc_id,
            "product_id": product_id
        }), 200

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
