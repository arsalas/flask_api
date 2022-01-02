from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/api/v1/users', methods=['GET'])
def get_users():
    response = {'message': 'success'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)