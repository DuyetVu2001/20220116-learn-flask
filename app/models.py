from datetime import datetime
from app import db


class Step(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mission_id = db.Column(db.Integer, db.ForeignKey(
        'mission.id'), nullable=False)
    start_point_id = db.Column(
        db.Integer, db.ForeignKey('point.id'), nullable=False)
    end_point_id = db.Column(
        db.Integer, db.ForeignKey('point.id'), nullable=False)

    def __repr__(self):
        return f"Step('{self.start_point_id}', '{self.end_point_id}')"


class Robot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"Robot('{self.name}')"


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    mission_id = db.Column(db.Integer, db.ForeignKey(
        'mission.id'), nullable=False)

    def __repr__(self):
        return f"Group('{self.name}')"


class Robot_Group(db.Model):
    robot_id = db.Column(db.Integer, db.ForeignKey(
        'robot.id'), primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey(
        'group.id'), primary_key=True)

    def __repr__(self):
        return f"robot_group('{self.robot_id}', '{self.group_id}')"


class Mission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    steps = db.relationship('Step', backref='mission', lazy=True)

    def __repr__(self):
        return f"Mission('{self.name}')"


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mission_id = db.Column(db.Integer, db.ForeignKey(
        'mission.id'), nullable=False)
    robot_id = db.Column(db.Integer, db.ForeignKey('robot.id'), nullable=False)

    def __repr__(self):
        return f"Order('{self.mission_id}', '{self.robot_id}')"
