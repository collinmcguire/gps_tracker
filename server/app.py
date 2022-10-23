from http import server
from flask import Flask, jsonify
from dotenv import load_dotenv
from numpy import true_divide
from pathlib import Path
import json, os

## Import dotenv variables
load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

activityData = os.getenv('activityData')

# Initialize server
app = Flask(__name__)

# Routes
@app.route('/showcoords')
def showcoords(): 
  records = []
  coords = {}

  ## Open json file
  with open(activityData, 'r') as f:
      data = f.read()
      records = json.loads(data)
      
      ## For every geopoint in the file parse it into a new variable
      for record in records:
        coords = []
        
        return record['geoPoints']


app.run(debug=True, threaded=True)