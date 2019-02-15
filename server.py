from flask import Flask, request, jsonify
from controller.api_helper import train_n_load, extract_info, load_all

application = Flask(__name__)

load_all()


# Training Api
@application.route('/train', methods=['POST'])
def train():
    return jsonify(train_n_load(request.get_json()))


# Parsing Api
@application.route('/parse', methods=['POST'])
def parse_query():
    return jsonify(extract_info(request.get_json()))


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5001)
