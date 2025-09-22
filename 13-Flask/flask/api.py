# Flask imports
from flask import Flask, jsonify, request

# Create the Flask application
app = Flask(__name__)

# =========================================
# Initial data in the to-do list
# Keep keys in lowercase for consistency
# =========================================
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

# =========================================
# Home route
# =========================================
@app.route('/')
def home():
    return "Welcome to the Sample To-Do List App"

# =========================================
# GET: Retrieve all the items
# =========================================
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)  # jsonify() converts Python data to JSON for API responses

# =========================================
# GET: Retrieve a specific item by ID
# <int:item_id> → Flask automatically converts the URL part into an integer
# =========================================
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    # Find the first matching item or return None
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

# =========================================
# POST: Create a new task - API
# =========================================
@app.route('/items', methods=['POST'])
def create_item():
    # Ensure request body is JSON and contains "name"
    if not request.json or 'name' not in request.json:
        return jsonify({"error": "Missing 'name' field"}), 400
    
    # Create a new item (id is incremented automatically)
    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json['name'],
        "description": request.json.get("description", "")  # default empty if not provided
    }
    items.append(new_item)
    return jsonify(new_item), 201  # 201 = Created

# =========================================
# PUT: Update an existing item
# =========================================
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404

    # Update fields only if they exist in request
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    
    return jsonify(item)

# =========================================
# DELETE: Delete an item
# =========================================
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    # Keep only the items whose id is NOT the one to delete
    items = [i for i in items if i["id"] != item_id]
    return jsonify({"result": "Item Deleted"})

# =========================================
# Run the app
# =========================================
if __name__ == '__main__':
    app.run(debug=True)
