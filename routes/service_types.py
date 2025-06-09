# routes/service_types.py

from flask import Blueprint, jsonify
from firebase_admin import firestore

service_types_bp = Blueprint('service_types_bp', __name__)
db = firestore.client()

def format_response(data_list):
    return jsonify({
        "status": "success",
        "data": data_list
    })

@service_types_bp.route('/api/service_types', methods=['GET'])
def get_service_types():
    try:
        docs = db.collection('service_types').stream()
        service_types = []
        for doc in docs:
            data = doc.to_dict()
            service_types.append({
                "service_type_id": data.get("service_type_id"),
                "service_type_nm": data.get("service_type_nm")
            })
        return format_response(service_types), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@service_types_bp.route('/api/brands/<service_type_id>', methods=['GET'])
def get_brands(service_type_id):
    try:
        docs = db.collection('brands').where('service_type_id', '==', service_type_id).stream()
        brands = []
        for doc in docs:
            data = doc.to_dict()
            brands.append({
                "brand_id": data.get("brand_id"),
                "brand_name": data.get("brand_name")
            })
        return format_response(brands), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@service_types_bp.route('/api/products/<brand_id>', methods=['GET'])
def get_products(brand_id):
    try:
        docs = db.collection('products').where('brand_id', '==', brand_id).stream()
        products = []
        for doc in docs:
            data = doc.to_dict()
            products.append({
                "product_id": data.get("product_id"),
                "product_nm": data.get("product_nm")
            })
        return format_response(products), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
