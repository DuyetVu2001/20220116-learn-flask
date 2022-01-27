from app import db


class Order(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    robot_id   = db.Column(db.Integer, db.ForeignKey('robot.id'), nullable=False)
    mission_id = db.Column(db.Integer, db.ForeignKey('mission.id'), nullable=False)

    def __repr__(self):
        return f"Order('{self.mission_id}', '{self.robot_id}')"
