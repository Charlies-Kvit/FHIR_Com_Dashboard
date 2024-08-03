from . import db_session
from flask_restful import abort, Resource, reqparse
from .account import Account
from flask import jsonify

parser = reqparse.RequestParser()
parser.add_argument("name")
parser.add_argument("email")
parser.add_argument("avatar_url")
parser.add_argument("group_id")


def abort_id_account_not_found(account_id):
    db_sess = db_session.create_session()
    group = db_sess.query(Account).get(account_id)
    db_sess.close()
    if not group:
        abort(404, message=f"Group {account_id} not found")


class AccountResource(Resource):
    def get(self, account_id):
        abort_id_account_not_found(account_id)
        db_sess = db_session.create_session()
        account = db_sess.query(Account).get(account_id)
        db_sess.close()
        return jsonify(
            {"account": account.to_dict(only=("id", "name", "email", "group_id", "avatar_url"))}
        )

    def put(self, account_id):
        abort_id_account_not_found(account_id)
        db_sess = db_session.create_session()
        args = parser.parse_args()
        account = db_sess.query(Account).get(account_id)
        account.name = args['name']
        account.email = args['email']
        account.group_id = args['group_id']
        account.avatar_url = args["avatar_url"]
        db_sess.commit()
        db_sess.close()
        return {"success": "OK"}

    def delete(self, account_id):
        abort_id_account_not_found(account_id)
        db_sess = db_session.create_session()
        account = db_sess.query(Account).get(account_id)
        db_sess.delete(account)
        db_sess.commit()
        db_sess.close()
        return {"success": "OK"}


class AccountListResource(Resource):
    def get(self):
        db_sess = db_session.create_session()
        accounts = db_sess.query(Account).all()
        db_sess.close()
        return jsonify({
            "accounts":
                [account.to_dict(only=("id", "name", "email", "group_id", "avatar_url")) for account in accounts]
        })

    def post(self):
        db_sess = db_session.create_session()
        args = parser.parse_args()
        account = Account(
            name=args['name'],
            email=args['email'],
            group_id=args['group_id'],
            avatar_url=args["avatar_url"]
        )
        db_sess.add(account)
        db_sess.commit()
        db_sess.close()
        return {'success': "OK"}
