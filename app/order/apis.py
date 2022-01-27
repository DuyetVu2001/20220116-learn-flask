from flask import Blueprint, request, jsonify
from app import db
from app.order.models import Order
from app.utils import as_dict


bp = Blueprint('orders', __name__)


@bp.route('/order')
def get_all_orders():
    try:
        orders = Order.query.all()
        return jsonify([as_dict(order) for order in orders])
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('/order', methods=['POST'])
def create_order():
    try:
        body = request.get_json()
        order = Order(**body)
        db.session.add(order)
        db.session.commit()
        return jsonify(as_dict(order)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@bp.route('/order/<int:id>', methods=['PUT'])
def update_order(id):
    try:
        body = request.get_json()
        order = Order.query.get(id)

        if not order:
            return jsonify({'message': 'No order found'}), 404
        for key, value in body.items():
            setattr(order, key, value)

        db.session.commit()
        return jsonify(as_dict(order)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@bp.route('/order/<int:id>', methods=['DELETE'])
def delete_order(id):
    try:
        existOrder = Order.query.get(id)

        if not existOrder:
            return jsonify({'message': 'No order found'}), 404

        db.session.delete(existOrder)
        db.session.commit()

        return jsonify({"message": "Order deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
