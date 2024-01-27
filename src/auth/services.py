import os
import jwt, datetime

secret_key = os.getenv("APP_SECRET_KEY")

class AuthServices:
    def login(body):
        payload = {
            "user": body["user"],
            "exp": datetime.datetime.now() + datetime.timedelta(hours=1),
            "iat": datetime.datetime.now()
        }

        try:
            jwt_token = jwt.encode(payload, secret_key, algorithm="HS256")
        except Exception as e:
            print(e)
            return f"Error: {e}"
        return jwt_token
