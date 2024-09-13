from data_generator import *
from flask import Flask, jsonify

app = Flask(__name__)

synthetic_prices_data = generate_synthetic_prices()


@app.route('/prices', methods=['GET'])
def get_all_prices():
    return jsonify(synthetic_prices_data), 200


@app.route('/prices/<string:action_name>', methods=['GET'])
def get_prices_for_action(action_name):
    filtered_data = [entry for entry in synthetic_prices_data if entry['action'] == action_name]
    if not filtered_data:
        return jsonify({'message': 'Action not found'}), 404
    return jsonify(filtered_data), 200


if __name__ == '__main__':
    app.run(debug=True)

