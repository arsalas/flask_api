import jwt

secretkey = "#SECRETKEY#"

def jwt_encode(payload):
    encoded_jwt = jwt.encode(payload, secretkey, algorithm="HS256")
    return encoded_jwt

def jwt_decode(token):
    try:
        decode_jwt = jwt.decode(token, secretkey, algorithms=["HS256"])
    except:
        decode_jwt = False
    return decode_jwt

