from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    if email == 'user@mail.com' and password == '123':
        return jsonify({'message': 'Login autorizado'}), 200
    else:
        return jsonify({'message': 'Login não autorizado'}), 401

if __name__ == '__main__':
    app.run(debug=True)