from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Flask Demo</h1>"

@app.route('/api')
def api():
    return jsonify({"message": "Hello from the API!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)