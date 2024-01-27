from flask import Flask

from src import routes

app = Flask(__name__)

# Routes 
routes(app)

if __name__ == "__main__":
    # Launch App
    app.run(debug=True)