from flask import request, jsonify

def startRoutesAuth(app):
    root = "/auth"
    @app.route(root + "/login", methods=["POST"])
    def login():
        params = request.get_json()
        return jsonify(params), 200
    
    @app.route(root + "/register", methods=["POST"])
    def register():
        params = request.get_json()
        return jsonify(params), 200

    
   
    
   
     

    
