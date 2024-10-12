from flask import Blueprint, jsonify, request

demoController = Blueprint("demoController", __name__, url_prefix="/api/demo")
users = []
@demoController.route('/get-all', methods=['GET'])
def subscriptionPlans():
    # Return Hello World message
    fat_133057 = "This is a simple local variable"
    return jsonify({'message': 'Hello, World! ' + fat_133057, 'statusCode': 200}), 200

@demoController.route('/users', methods=['POST'])
def create_user():
    new_user = {
        'id': request.args.get('id'),
        'name': request.args.get('name'),
        'email': request.args.get('email'),
    }
    users.append(new_user)
    return jsonify(new_user), 201

@demoController.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200


@demoController.route('/edituser/<int:id>', methods=['PUT'])
def update_user(id):
    idParam = request.json.get('id');
    # existingUserId = request.args.get('id'),
    for user in users:
        if user['id'] == idParam:
            user['name']= request.json.get('name')
            user['email']= request.json.get('email')
            return jsonify(user), 200
    return jsonify(), 302





