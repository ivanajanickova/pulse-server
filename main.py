from flask import Flask, jsonify
from flask_restful import request
import numpy as np


app = Flask(__name__)


def byes_to_arr(byte_array):
    loaded_np = np.frombuffer(byte_array, dtype=np.uint8)
    # TODO reshape `loaded_np`
    return loaded_np


@app.route('/test', methods=['PUT'])
def test():
    image_bytes = request.data
    decoded = byes_to_arr(image_bytes)
    if decoded is not None:
        return jsonify({'Status': 'Working OK'})
    else:
        return jsonify({'Status': 'Not recieved'})

if __name__ == '__main__':
    app.run(debug=True)

