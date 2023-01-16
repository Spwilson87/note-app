import os

from flask import Flask, render_template, redirect, url_for, flash, request
# flask migrate will create migration scripts to when making changes to db structure
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash

# This defines some default configs

def create_app(test_config=None):
    app = Flask(__name__)
    app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgresql://notes:notes1234@192.168.1.172:5432/notes'

    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', default='dev')
    )
# If test config is none then will use python file config.py

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    from .models import db, User
    
    db.init_app(app)
    migrate = Migrate(app, db)
    
    @app.route('/sign_up', methods=('GET', 'POST'))
    def sign_up():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            error = None
            
            if not username:
                error = 'Username is required.'
            elif not password:
                error = 'Password is required.'
            elif User.query.filter_by(username=username).first():
                error = 'Username already taken.'
                
            if error is None:
                user = User(username=username, password=generate_password_hash(password))
                db.session.add(user)
                db.session.commit()
                flash("Successfully signed up! Please log in.", 'success')
                return redirect(url_for('log_in'))
            
            flash(error, 'error')
                        
        return render_template('sign_up.html')
    
    @app.route('/log_in')
    def log_in():
        return 'Login'
        
        
    return app