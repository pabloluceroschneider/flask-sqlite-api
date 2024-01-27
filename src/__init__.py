from .auth import auth
from .users import users

def routes(app):
    app.register_blueprint(auth)
    app.register_blueprint(users)
    return app