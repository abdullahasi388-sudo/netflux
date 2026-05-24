#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask
app = Flask(__name__)
app.secret_key = 'netflux_secret_key_2024'

from auth_routes    import auth_bp
from content_routes import content_bp
from api_routes     import api_bp

app.register_blueprint(auth_bp)
app.register_blueprint(content_bp)
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=int(os.environ.get('PORT', 5000)))
