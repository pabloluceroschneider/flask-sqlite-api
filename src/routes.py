from .auth import routes as authRoutes
from .users import routes as userRoutes

def routes(app):
    app.register_blueprint(authRoutes.auth)
    app.register_blueprint(userRoutes.users)
    return app