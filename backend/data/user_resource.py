from . import db_session
from flask_restful import abort, Resource, reqparse
from .users import User
from flask import abort, jsonify

parser = reqparse.RequestParser()
parser.add_argument("name")
parser.add_argument("email")
parser.add_argument("avatar_url")
parser.add_argument("group_id")


def abort_id_user_not_found(user_id):
    db_sess = db_session.create_session()
    group = db_sess.query(User).get(user_id)
    db_sess.close()
    if not group:
        abort(404, f"Group {user_id} not found")


class UserResource(Resource):
    def get(self, user_id):
        abort_id_user_not_found(user_id)
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(user_id)
        db_sess.close()
        return jsonify(
            {"user": user.to_dict(only=("id", "name", "email", "group_id", "avatar_url"))}
        )

    def put(self, user_id):
        abort_id_user_not_found(user_id)
        db_sess = db_session.create_session()
        args = parser.parse_args()
        user = db_sess.query(User).get(user_id)
        user.name = args['name']
        user.email = args['email']
        user.group_id = args['group_id']
        user.avatar_url = args["avatar_url"]
        db_sess.commit()
        db_sess.close()
        return {"success": "OK"}

    def delete(self, user_id):
        abort_id_user_not_found(user_id)
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(user_id)
        db_sess.delete(user)
        db_sess.commit()
        db_sess.close()
        return {"success": "OK"}


class UserListResource(Resource):
    def get(self):
        db_sess = db_session.create_session()
        users = db_sess.query(User).all()
        db_sess.close()
        return jsonify({
            "users":
                [user.to_dict(only=("id", "name", "email", "group_id", "avatar_url")) for user in users]
        })

    def post(self):
        db_sess = db_session.create_session()
        args = parser.parse_args()
        user = User(
            name=args['name'],
            email=args['email'],
            group_id=args['group_id'],
            avatar_url=args["avatar_url"]
        )
        db_sess.add(user)
        db_sess.commit()
        db_sess.close()
        return {'success': "OK"}
