from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from app import db

class LostItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    description = db.Column(db.Text)
    location = db.Column(db.String(100))
    date_lost = db.Column(db.Date)
    image_filename = db.Column(db.String(100))
    date_reported = db.Column(db.DateTime, default=datetime.utcnow)

class FoundItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    description = db.Column(db.Text)
    location = db.Column(db.String(100))
    date_found = db.Column(db.Date)
    image_filename = db.Column(db.String(100))
    date_reported = db.Column(db.DateTime, default=datetime.utcnow)
