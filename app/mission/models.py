from app import db


class Step(db.Model):
    id             = db.Column(db.Integer, primary_key=True)
    mission_id     = db.Column(db.Integer, db.ForeignKey('mission.id'), nullable=False)
    end_point_id   = db.Column(db.Integer, db.ForeignKey('point.id'), nullable=False)
    start_point_id = db.Column(db.Integer, db.ForeignKey('point.id'), nullable=False)

    def __repr__(self):
        return f"Step('{self.start_point_id}', '{self.end_point_id}')"


class Mission(db.Model):
    id    = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(50), unique=True, nullable=False)
    steps = db.relationship('Step', backref='mission', lazy=False)

    def __repr__(self):
        return f"Mission('{self.name}')"
