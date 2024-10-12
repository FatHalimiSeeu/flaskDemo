from flask import Flask
from controller.demoController import demoController
app = Flask(__name__)
app.register_blueprint(demoController)

@app.route('/')  # Using this method for testing purposes
def hello_world():
    data = "This is a message straight from main"
    return data



if __name__ == '__main__':
    # serve(app, host="0.0.0.0", port=5000)
    app.run(host='0.0.0.0', port=5000)
