from flask import Blueprint, make_response, request
from app import db, bcrypt
from app.user.models import User
from app.utils import as_dict


bp = Blueprint('users', __name__)


@bp.route("/register", methods=['POST'])
def register():
    body = request.get_json()

    # rewrite all conditions here
    if not body or not body.get('username') and not body.get('password'):
        return {"message": "Missing username or password"}, 400

    checkUser = User.query.filter_by(username=body.get('username')).first()
    if checkUser:
        return {"message": "Username already exists"}, 409

    hashed_password = bcrypt.generate_password_hash(
        body.get('password')).decode('utf-8')

    user = User(username=body.get('username'), password=hashed_password)
    db.session.add(user)
    db.session.commit()

    return {"message": "Successfully registered"}, 201


@bp.route("/login", methods=['POST'])
def login():
    body = request.get_json()

    if not body or not body.get('username') or not body.get('password'):
        return {"message": "Missing username or password"}, 400

    user = User.query.filter_by(username=body.get('username')).first()
    if not user:
        return {"message": "User does not exist"}, 404

    if bcrypt.check_password_hash(user.password, body.get('password')):
        return {"message": "Login successfully!"}, 200
    else:
        return {"message": "Invalid credentials"}, 401


@bp.route("/users")
def users():
    page = request.args.get('page', 1, type=int)
    print(page)

    users = User.query.order_by(
        User.created.asc()).paginate(page=page, per_page=1)

    print(users.items)

    return make_response({
        "data": [as_dict(user) for user in users.items]
    }, 200)
