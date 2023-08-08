from app.models.db import db


class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # 'employee' or 'manager'
    
    supervisor_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    vacations = db.relationship('Vacation', backref='user', lazy=True)
    employees = db.relationship('User', backref=db.backref('supervisor', remote_side=[id]), lazy=True)