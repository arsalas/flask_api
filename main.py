from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

from helpers.sockets import startSockets
from routes import startRoutes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
cors = CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")
startRoutes(app)
startSockets(socketio)
socketio.run(app)
