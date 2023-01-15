import os

from flask import Flask, render_template
# flask migrate will create migration scripts to when making changes to db structure
from flask_migrate import Migrate

# This defines some default configs

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', default='dev')
    )
# If test config is none then will use python file config.py

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    from .models import db
    
    db.init_app(app)
    migrate = Migrate(app, db)
    
    @app.route('/sign_up')
    def sign_up():
        return render_template('sign_up.html')
    return app