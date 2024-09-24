from . import db_session
from flask_restful import abort, Resource, reqparse
from .account import Account
from flask import jsonify
from threading import Thread
from parsing.main_parse import main
from .parse_result import ParseResult
import time

parser = reqparse.RequestParser()
parser.add_argument("name")
parser.add_argument("email")
parser.add_argument("avatar_url")
parser.add_argument("group_id")
parser.add_argument("zulip_id")


def parse_new_account(email, zulip_id):
    result = main([email], {email: zulip_id})
    db_sess = db_session.create_session()
    for el in result[email]:
        account = db_sess.query(Account).filter(Account.email == email).first()
        parse_result = ParseResult(
            text=el["text"],
            title=el["title"],
            timestamp=int(el["timestamp"]),
            last_parsing_time=time.time(),
            account_email=email,
            account_post_count=el["count"],
            url=el["url"],
            account_id=account.id
        )
        db_sess.add(parse_result)
        db_sess.commit()
    db_sess.close()


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
            {"account": account.to_dict(only=("id", "name", "email", "group_id", "avatar_url", "zulip_id"))}
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
        account.zulip_id = args["zulip_id"]
        db_sess.commit()
        account = db_sess.query(Account).get(account_id)
        db_sess.close()
        return jsonify(
            {"account": account.to_dict(only=("id", "name", "email", "group_id", "avatar_url", "zulip_id"))}
        )

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
                [account.to_dict(only=("id", "name", "email", "group_id", "avatar_url", "zulip_id"))
                 for account in accounts]
        })

    def post(self):
        db_sess = db_session.create_session()
        args = parser.parse_args()
        account = Account(
            name=args['name'],
            zulip_id=args['zulip_id'],
            email=args['email'],
            group_id=args['group_id'],
            avatar_url=args["avatar_url"]
        )
        db_sess.add(account)
        db_sess.commit()
        account = db_sess.query(Account).filter(Account.email == args["email"]).first()
        db_sess.close()
        parsing = Thread(target=parse_new_account, args=(args["email"], args['zulip_id'], ))
        parsing.start()
        return jsonify(
            {"account": account.to_dict(only=("id", "name", "email", "group_id", "avatar_url", "zulip_id"))}
        )
