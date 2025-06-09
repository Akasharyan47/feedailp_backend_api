from flask import Blueprint, jsonify, request
from firebase_admin import firestore
import hashlib

submit_review_bp = Blueprint('submit_review_bp', __name__)
db = firestore.client()

def generate_3digit_id(email: str, product_id: str) -> str:
    unique_str = email.lower() + "_" + product_id
    hash_bytes = hashlib.sha256(unique_str.encode()).digest()
    hash_int = int.from_bytes(hash_bytes[:4], 'big')
    id_num = hash_int % 1000
    return f"{id_num:03d}"  # zero-padded 3-digit string

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

        try:
            product_id = data['product']['product']['product_id']
        except Exception:
            return jsonify({
                "status": "error",
                "message": "Invalid product structure or missing product_id"
            }), 400

        # Generate 3-digit unique ID based on email + product_id
        doc_id = generate_3digit_id(data['email'], product_id)

        # Prepare data to save including the user name
        review_data = {
            "product": data['product'],
            "District": data['District'],
            "Star_Ratings": data['Star_Ratings'],
            "Yes_No": data['Yes_No'],
            "email": data['email'],
            "name": data['name'],    # Store actual user name here
            "reviewText": data['reviewText'],
            "timestamp": firestore.SERVER_TIMESTAMP
        }

        # Save to Firestore with doc_id = 3-digit ID
        db.collection("reviews").document(doc_id).set(review_data)

        return jsonify({
            "status": "success",
            "message": f"Review submitted successfully with ID {doc_id}!",
            "doc_id": doc_id,
            "user_name": data['name']  # Return the user name as well
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
