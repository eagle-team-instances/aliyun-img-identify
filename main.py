from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def uploadHandler():
    return jsonify([{'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}])
