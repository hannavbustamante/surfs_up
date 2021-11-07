# Import the Flask dependency
from flask import Flask

# Create new Flask instance
app = Flask(__name__)

# Create Flask routes

# Root
@app.route('/')
def hello_world():
    return 'Hello World'