import os
from .config import config
from .routes import routes
from . import create_app

app = create_app(os.getenv("CONFIG_MODE"))

# Routes 
routes(app)

if __name__ == "__main__":
    scope = config["CONFIG_MODE"]
    app.config.from_object(scope)

    # Launch App
    app.run()