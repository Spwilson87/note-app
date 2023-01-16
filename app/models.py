from flask_sqlalchemy import SQLAlchemy

db = SQLALCHEMY()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200))
    
    # makes timestapes for when user created or updtaed
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    # this links the notes with the user who created them
    notes = db.relationship('Note', backref='author', lazy=True)
    
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    body = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    # this assigns a users id to note from the user class
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
