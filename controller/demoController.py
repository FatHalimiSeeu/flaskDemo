from flask import Blueprint, jsonify

demoController = Blueprint("demoController", __name__, url_prefix="/api/demo")

@demoController.route('/get-all', methods=['GET'])
def subscriptionPlans():
    # Return Hello World message
    fat_133057 = "This is a simple local variable"
    return jsonify({'message': 'Hello, World! ' + fat_133057, 'statusCode': 200}), 200





