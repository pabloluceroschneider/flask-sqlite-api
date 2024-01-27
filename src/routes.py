from .auth import auth
from .users import routes as userRoutes

def routes(app):
    app.register_blueprint(auth)
    app.register_blueprint(userRoutes.users)
    return app