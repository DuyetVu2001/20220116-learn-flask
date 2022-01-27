from flask import Blueprint, request, jsonify
from app import db
from app.mission.models import Mission, Step
from app.utils import as_dict


bp = Blueprint('missions', __name__)


@bp.route('/mission')
def get_all_mission():
    missions = Mission.query.all()

    return jsonify([as_dict(mission) for mission in missions]), 200


@bp.route('/step')
def get_all_step():
    steps = Step.query.all()
    return jsonify([as_dict(step) for step in steps]), 200


@bp.route('/mission', methods=['POST'])
def create_mission():
    body = request.get_json()

    checkMission = Mission.query.filter_by(name=body['name']).first()
    if checkMission:
        return jsonify({'message': 'Mission already exists'}), 400

    if not body:
        return jsonify({'message': 'No input data provided'}), 400
    elif not all(key in body for key in ('name', 'steps')):
        return jsonify({'message': 'Missing data'}), 400

    mission = Mission(name=body['name'])
    db.session.add(mission)
    db.session.commit()

    for step in body['steps']:
        if not all(key in step for key in ('start_point_id', 'end_point_id')):
            db.session.delete(mission)
            db.session.commit()
            return jsonify({'message': 'Missing data'}), 400

        step = Step(start_point_id=step['start_point_id'],
                    end_point_id=step['end_point_id'], mission_id=mission.id)

        db.session.add(step)

    db.session.commit()
    return jsonify({'message': f'Created mission {mission.name} successfully!'}), 201


@bp.route('/mission/<int:id>', methods=['PUT'])
def update_mission(id):
    body = request.get_json()

    mission = Mission.query.get(id)
    if not mission:
        return jsonify({'message': 'Mission not found'}), 404

    if not body:
        return jsonify({'message': 'No input data provided'}), 400
    elif not all(key in body for key in ('name', 'steps')):
        return jsonify({'message': 'Missing data'}), 400

    mission.name = body['name']

    for step in body['steps']:
        if not all(key in step for key in ('start_point_id', 'end_point_id')):
            return jsonify({'message': 'Missing data'}), 400

        # if update mission with new step
        if not step.get('id'):
            step = Step(start_point_id=step['start_point_id'],
                        end_point_id=step['end_point_id'], mission_id=mission.id)
            db.session.add(step)

        # if update mission with existing step
        else:
            exitStep = Step.query.get(step['id'])
            exitStep.start_point_id = step['start_point_id']
            exitStep.end_point_id = step['end_point_id']

    db.session.commit()
    return jsonify({'message': f'Updated mission \'{mission.name}\' successfully!'}), 200


@bp.route('/mission/<int:id>', methods=['DELETE'])
def delete_mission(id):
    try:
        mission = Mission.query.get(id)
        if not mission:
            return jsonify({'message': 'Mission not found'}), 404

        db.session.delete(mission)

        for step in mission.steps:
            db.session.delete(step)

        db.session.commit()

        return jsonify({'message': f'Deleted mission \'{mission.name}\' successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500
