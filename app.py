from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask CI/CD Project!"

@app.route('/users')
def users():
    return jsonify({"users": ["satwika", "sweety", "snehitha"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
