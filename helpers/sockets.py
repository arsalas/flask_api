from flask_socketio import send, emit

def startSockets(socketio):
    
    @socketio.on('connect')
    def assignRoom():
        print('connect')
        
        
    @socketio.on('myevent')
    def handlemessage(msg):
        print(msg)
        send(msg, broadcast = True)
        emit('test', msg, broadcast = True)
        
    