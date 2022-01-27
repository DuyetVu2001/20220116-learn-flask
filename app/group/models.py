from app import db


class Group(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(50), unique=True, nullable=False)
    mission_id = db.Column(db.Integer, db.ForeignKey('mission.id'), nullable=True)    
    robots     = db.relationship('Robot', backref='group', lazy=False)

    def __repr__(self):
        return f"Group('{self.name}')"
