from unicodedata import name
from flask import Blueprint, request, jsonify
from app import db
from app.group.models import Group
from app.robot.models import Robot
from app.utils import as_dict
# from sqlalchemy.exc import ProgrammingError


bp = Blueprint('groups', __name__)


@bp.route('/group')
def get_all_groups():
    try:
        groups = Group.query.all()
        if groups:
            for group in groups:
                print(group.robots)
        
        return jsonify([as_dict(group) for group in groups])
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('/group', methods=['POST'])
def create_group():
    try:
        body = request.get_json()
        if not body:
            return jsonify({'message': 'No input data provided'}), 400
        
        existGroup = Group.query.filter_by(name=body['name']).first()
        if existGroup:
            return jsonify({'message': 'Group already exists'}), 409

        group = Group(name=body['name'], mission_id=body['mission_id'])
        db.session.add(group)

        for robot_id in body['robots_id']:
            robot = Robot.query.get(robot_id)
            if robot:
                group.robots.append(robot)

        db.session.commit()
        return jsonify(as_dict(group)), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@bp.route('/group/<int:id>', methods=['PUT'])
def update_group(id):
    try:
        body = request.get_json()
        group = Group.query.get(id)

        if not group:
            return jsonify({'message': 'No group found'}), 404
        for key, value in body.items():
            setattr(group, key, value)

        db.session.commit()
        return jsonify(as_dict(group)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@bp.route('/group/<int:id>', methods=['DELETE'])
def delete_group(id):
    try:
        existGroup = Group.query.get(id)

        if not existGroup:
            return jsonify({'message': 'No group found'}), 404

        db.session.delete(existGroup)
        db.session.commit()

        return jsonify({"message": "Deleted successfully!"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
