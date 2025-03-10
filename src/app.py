from flask import  Flask, request, jsonify

app = Flask(__name__)

# Banco de dados fictício
users = []

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "invalid data"}), 400

    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "email": data["email"]
    }

    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

@app.route('/users/<int:user_id>', methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"Message": "User deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)

