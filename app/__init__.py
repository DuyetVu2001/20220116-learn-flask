from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from app.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)

    from app.user.apis import bp as users
    from app.point.apis import bp as points
    from app.mission.apis import bp as missions
    from app.robot.apis import bp as robots
    from app.group.apis import bp as groups
    from app.order.apis import bp as orders

    app.register_blueprint(users)
    app.register_blueprint(points)
    app.register_blueprint(missions)
    app.register_blueprint(robots)
    app.register_blueprint(groups)
    app.register_blueprint(orders)

    return app
