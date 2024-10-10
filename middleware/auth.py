import os
from functools import wraps
from flask import request, jsonify
def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        secret_jwt = os.getenv('SECRET_JWT')

        if not auth_header:
            return jsonify({'message': 'Authorization header is missing'}), 401

        # token_type, token = auth_header.split(None, 1)
        token = auth_header

        # Verify and decode the token
        try:
            # decoded_token = jwt.decode(token, secret_jwt, algorithms=['HS256'])
            user_id = 2
            # existing_user = db_session.query(EdukistUsers).get(user_id)
            existing_user_token = "Fat"
            if existing_user_token != token:
                return jsonify({'message': 'Invalid token for the user'}), 401
        except exit():
            return jsonify({'message': 'Token has expired'}), 401

        # Call the decorated function
        return func(*args, **kwargs)

    return wrapper

