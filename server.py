# Code adapated from https://github.com/andrewbeattycourseware/datarepresentation2021
from orderDAO import orderDao
from flask import Flask, url_for, request, redirect, abort,jsonify

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
   return  "Check Customer Order"

#curl http://127.0.0.1:5000/customerOrder
@app.route('/customerOrder')
def getAll():
   return jsonify(orderDao.getAll())

#curl http://127.0.0.1:5000/customerOrder/3
@app.route('/customerOrder/<int:id>') 
def findById(id): 
    return jsonify(orderDao.findById(id))


#curl -X POST -d "{\"name\":\"Xavier Chan\", \"item\":\"Keyboard\", \"price\":50}" -H "Content-Type:application/json" http://127.0.0.1:5000/customerOrder
@app.route('/customerOrder', methods=['POST'])
def create(): 

    if not request.json: #abort the request if not in the correct json format
        abort(400)
    
    # append the order with a new id and so on, if good request
    order = {
        #"id":request.json["id"], not required as mysqldb is auto-incremented
        "name": request.json["name"],
        "item": request.json["item"],
        "price": request.json["price"]
    }

    return jsonify(orderDao.create(order))   



#curl -X PUT -d "{\"name\":\"Xavier Chen\", \"item\":\"Mouse\", \"price\":25}" -H "Content-Type:application/json" http://127.0.0.1:5000/customerOrder/3
@app.route('/customerOrder/<int:id>', methods=['PUT'])
def update(id):
    foundItem=orderDao.findById(id)
    print(foundItem)
    if foundItem == {}:#if found nothing with the id,  error code 404 shows up on the server, {} on the screen.
        return jsonify({}), 404
    currentItem = foundItem
    if 'name' in request.json:
        currentItem['name'] = request.json['name']
    if 'item' in request.json:
        currentItem['item'] = request.json['item']
    if 'price' in request.json:
        currentItem['price'] = request.json['price']
    orderDao.update(currentItem)
    return jsonify(currentItem)


# curl -X DELETE http://127.0.0.1:5000/customerOrder/3
@app.route('/customerOrder/<int:id>', methods=['DELETE'])
def delete(id):
    orderDao.delete(id)
    return jsonify({"done":True})

if __name__ == "__main__":
    app.run(debug=True)