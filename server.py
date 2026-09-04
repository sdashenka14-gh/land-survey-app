from flask import Flask, jsonify, request
from flask_cors import CORS
from shapely.geometry import shape

app = Flask(__name__)
CORS(app)

parcels = []

@app.route('/parcels', methods=['GET'])
def get_parcels():
    return jsonify(parcels)

@app.route('/add', methods=['POST'])
def add_parcel():
    new_parcel = request.json
    new_shape = shape(new_parcel['boundary'])

    for existing in parcels:
        existing_shape = shape(existing['boundary'])
        if new_shape.intersects(existing_shape):
            new_parcel['status'] = 'disputed'
            existing['status'] = 'disputed'

    if 'status' not in new_parcel:
        new_parcel['status'] = 'verified'

    parcels.append(new_parcel)
    return jsonify({'saved': True, 'status': new_parcel['status']})

if __name__ == "__main__":
    app.run(debug=True)