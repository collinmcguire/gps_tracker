from http import server
from flask import Flask

# Initialize server
app = Flask(__name__)

# Routes
@app.route('/')

def hello_world():
  return 'Hello World!'
  