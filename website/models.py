from . import db
from flask_login import UserMixin, current_user
import datetime
from sqlalchemy.sql import func

td = datetime.date.today()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    user_name = db.Column(db.String(150))
    order =db.relationship('Order')


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(150))
    collector_name = db.Column(db.String(150))
    mango = db.Column(db.Integer, default=0)
    orange = db.Column(db.Integer, default=0)
    banana = db.Column(db.Integer, default=0)
    day = db.Column(db.Integer, default=td.day)
    month = db.Column(db.Integer, default=td.month)
    year = db.Column(db.Integer, default=td.year)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class R_code(db.Model):
    
    email = db.Column(db.String(50), primary_key = True)