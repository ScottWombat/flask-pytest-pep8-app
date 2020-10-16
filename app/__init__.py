from flask import Flask, jsonify

app = Flask(__name__)

def create_app(config_filename=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    return app
   
      
@app.route("/")
def index():
    return jsonify({'hello':'world'})   
    
