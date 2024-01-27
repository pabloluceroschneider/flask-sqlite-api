from flask import Flask
from config import config

from src import routes

app = Flask(__name__)

# Routes 
routes(app)

if __name__ == "__main__":
    scope = config["CONFIG_MODE"]
    app.config.from_object(scope)

    # Launch App
    app.run()