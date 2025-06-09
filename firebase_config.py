# BackendAPI/firebase_config.py

import base64
import json
from firebase_admin import credentials, initialize_app, firestore

def init_firestore():
    with open('firebase-encoded.txt', 'r') as f:
        encoded_cred = f.read().strip()

    decoded_cred = base64.b64decode(encoded_cred).decode('utf-8')
    cred_dict = json.loads(decoded_cred)

    cred = credentials.Certificate(cred_dict)

    try:
        initialize_app(cred)
    except ValueError:
        # Already initialized
        pass

    return firestore.client()
