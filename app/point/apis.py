from flask import Blueprint, request, make_response, jsonify
from app import db
from app.point.models import Point
from app.utils import as_dict


bp = Blueprint('points', __name__)


@bp.route("/point")
def get_all_point():
    points = Point.query.all()
    print()
    return make_response({
        "data": [as_dict(point) for point in points]
    }, 200)


@bp.route("/point", methods=['POST'])
def create_point():
    body = request.get_json()

    if not body or not body.get('name'):
        return make_response(jsonify({"message": "Missing name field!"}), 400)

    point = Point.query.filter_by(name=body["name"]).first()
    if point:
        return {"message": "Point already exists"}, 409

    point = Point(name=body["name"])
    db.session.add(point)
    db.session.commit()

    return make_response({"message": "Successfully created point"}, 201)


@bp.route("/point/<int:id>", methods=['PUT'])
def update_point(id):
    body = request.get_json()
    if not body or not body.get('name'):
        return {"message": "Missing name field"}, 400

    point = Point.query.get(id)
    if not point:
        return {"message": "Point does not exist"}, 404

    point.name = body["name"]
    db.session.commit()
    return {"message": "Successfully updated point"}, 200


@bp.route("/point/<int:id>", methods=['DELETE'])
def delete_point(id):
    point = Point.query.get(id)
    if not point:
        return {"message": "Point does not exist"}, 404

    db.session.delete(point)
    db.session.commit()

    return {"message": "Successfully deleted point"}, 200
