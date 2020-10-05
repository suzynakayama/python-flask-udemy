from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My First Store',
        'items': [
            {
                'name': 'Item 1',
                'price': 15.99
            },
            {
                'name': 'Item 2',
                'price': 99
            },
            {
                'name': 'Item 3',
                'price': 15
            }
        ]
    },
    {
        'name': 'My Second Store',
        'items': [
            {
                'name': 'Item 4',
                'price': 9
            },
            {
                'name': 'Item 5',
                'price': 25
            },
            {
                'name': 'Item 6',
                'price': 30
            },
        ]
    },
]

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'store': store})
    return jsonify({'message': 'store not found'})

@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price'],
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found.'})

@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found.'})

app.run(port=3005)      # choose the port you want to run the app

