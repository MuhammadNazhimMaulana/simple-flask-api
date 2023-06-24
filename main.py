from flask import Flask, request, render_template, jsonify
from flask_restful import Api
from flask_cors import CORS
from blueprints.API.routes import initialize_routes
from blueprints.Home.home import home_bp
import os

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

# Register
app.register_blueprint(home_bp)

# API
initialize_routes(api)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)