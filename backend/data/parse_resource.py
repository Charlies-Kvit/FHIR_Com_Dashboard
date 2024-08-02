from . import db_session
import time
import requests
from flask_restful import abort, Resource, reqparse
from .parse_result import ParseResult
from .account import Account
from parsing.main_parse import main

parser = reqparse.RequestParser()
parser.add_argument("emails", action="append", required=True)


def abort_id_account_not_found(account_email):
    db_sess = db_session.create_session()
    group = db_sess.query(ParseResult).filter(ParseResult.account_email == account_email).first()
    db_sess.close()
    if not group:
        abort(404, message=f"Account {account_email} not found")


class ParseRequestResource(Resource):
    def get(self, account_email):
        abort_id_account_not_found(account_email)
        db_sess = db_session.create_session()
        parse_res = db_sess.query(ParseResult).filter(ParseResult.account_email == account_email).first()
        db_sess.close()
        return parse_res.to_dict(only=("id", "title", "url", "account_post_count", "text", "account_id"))

    def put(self, account_email):
        pass


class ParseRequestListResource(Resource):
    def post(self):
        args = parser.parse_args()
        emails = args["emails"]
        """start_time = args["start_time"]
        end_time = args["end_time"]"""
        get_emails = []
        do_emails = []
        db_sess = db_session.create_session()
        for email in emails:
            parse_res = db_sess.query(ParseResult).filter(ParseResult.account_email == email).first()
            if not parse_res:
                get_emails.append(email)
                continue
            do_emails.append(email)
        result = main(get_emails)
        for email in get_emails:
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
        return {"success": "OK"}
