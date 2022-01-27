from flask import Blueprint, request, jsonify
from app import db
from app.robot.models import Robot
from app.utils import as_dict
# from sqlalchemy.exc import ProgrammingError


bp = Blueprint('robots', __name__)


@bp.route('/robot')
def get_all_robots():
    robots = Robot.query.all()
    return jsonify([as_dict(robot) for robot in robots])


@bp.route('/robot', methods=['POST'])
def create_robot():
    try:
        existRobot = Robot.query.filter_by(name=request.json['name']).first()
        if existRobot:
            return jsonify({'message': 'Robot already exists'}), 409

        body = request.get_json()
        if not body:
            return jsonify({'message': 'No input data provided'}), 400

        # check if not have key "name"
        if 'name' not in body or body['name'] == '':
            return jsonify({'message': 'No \'name\' provided'}), 400

        robot = Robot(**body)

        db.session.add(robot)

        db.session.commit()
        return jsonify(as_dict(robot)), 201

    # except ProgrammingError as e:
    #     return jsonify({'message': 'Some errors'}), 500

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500


@bp.route('/robot/<int:id>', methods=['PUT'])
def update_robot(id):
    try:
        body = request.get_json()

        if not body:
            return jsonify({'message': 'No input data provided'}), 400
        if not body.get('name') or body['name'] == '':
            return jsonify({'message': 'No field \'name\' provided'}), 400

        robot = Robot.query.get(id)

        if not robot:
            return jsonify({'message': 'No robot found'}), 404

        for key, value in body.items():
            setattr(robot, key, value)

        db.session.commit()
        return jsonify({"message": "Updated successfully!"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500


@bp.route('/robot/<int:id>', methods=['DELETE'])
def delete_robot(id):
    try:
        existRobot = Robot.query.get(id)
        if not existRobot:
            return jsonify({'message': 'No robot found'}), 404

        db.session.delete(existRobot)
        db.session.commit()

        return jsonify({'message': 'Robot deleted'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500
