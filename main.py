from app import create_app, db

# from app.point.models import Point
# from app.mission.models import Mission
# from app.robot.models import Robot
# from app.group.models import Group

app = create_app()

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)
