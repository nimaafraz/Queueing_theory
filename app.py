from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# This is your food order simulation
orders = {"noodles": 0, "salad": 0, "rice": 0}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_order/<food_item>', methods=['POST'])
def add_order(food_item):
    if food_item in orders:
        orders[food_item] += 1
        return jsonify({"status": f"{food_item} added", "current_orders": orders})
    else:
        return jsonify({"status": "invalid food item", "current_orders": orders})

@app.route('/get_orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

if __name__ == "__main__":
    app.run(debug=True)
