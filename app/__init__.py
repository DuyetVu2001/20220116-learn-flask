from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://duyet:12345678@localhost/agv'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class Point(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


class Step(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mission_id = db.Column(db.Integer, db.ForeignKey(
        'mission.id'), nullable=False)
    start_point_id = db.Column(
        db.Integer, db.ForeignKey('point.id'), nullable=False)
    end_point_id = db.Column(
        db.Integer, db.ForeignKey('point.id'), nullable=False)


class Robot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    mission_id = db.Column(db.Integer, db.ForeignKey(
        'mission.id'), nullable=False)


class robot_group(db.Model):
    robot_id = db.Column(db.Integer, db.ForeignKey(
        'robot.id'), primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey(
        'group.id'), primary_key=True)


class Mission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mission_id = db.Column(db.Integer, db.ForeignKey(
        'mission.id'), nullable=False)
    robot_id = db.Column(db.Integer, db.ForeignKey('robot.id'), nullable=False)
