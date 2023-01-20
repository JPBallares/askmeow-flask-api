import os
from flask import jsonify, request, Blueprint, abort
from cryptography.fernet import Fernet
from core.split import SplitSDK

split = SplitSDK()
encryption_bp = Blueprint('encryption', __name__)

# Fernet encryption key
key = Fernet.generate_key()
cipher = Fernet(key)


@encryption_bp.route('/encrypt', methods=['POST'])
def encrypt_string():
    content = request.json['content']
    encrypted_string = cipher.encrypt(content.encode())
    return jsonify({
        'encrypted_string': encrypted_string.decode(),
    })
