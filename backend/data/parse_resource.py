from . import db_session
import time
from flask_restful import abort, Resource, reqparse
from .parse_result import ParseResult
from .account import Account
from parsing.main_parse import main

parser = reqparse.RequestParser()
parser.add_argument("emails", action="append", required=True)
parser.add_argument("zulip_ids", action="append", required=True)


def abort_id_account_not_found(account_id):
    db_sess = db_session.create_session()
    account = db_sess.query(ParseResult).filter(ParseResult.account_id == account_id).first()
    db_sess.close()
    if not account:
        abort(404, message=f"Account {account_id} not found")


class ParseRequestResource(Resource):
    def get(self, account_id):
        abort_id_account_not_found(account_id)
        db_sess = db_session.create_session()
        parse_results = db_sess.query(ParseResult).filter(ParseResult.account_id == account_id).all()
        db_sess.close()
        return {parse_results[0].account_email: [parse_res.to_dict(only=("id", "title", "url", "account_post_count", "text", "account_id", "timestamp"))
                for parse_res in parse_results]}

    def put(self, account_email):
        pass


class ParseRequestListResource(Resource):
    def post(self):
        args = parser.parse_args()
        emails = args["emails"]
        zulip_ids = args["zulip_ids"]
        data = {}
        for index, email in enumerate(emails):
            data[email] = zulip_ids[index]
        """start_time = args["start_time"]
        end_time = args["end_time"]"""
        get_emails = []
        do_emails = []
        db_sess = db_session.create_session()
        answer = []
        for email in emails:
            parse_res = db_sess.query(ParseResult).filter(ParseResult.account_email == email).first()
            if not parse_res:
                get_emails.append(email)
                continue
            do_emails.append(email)
            if parse_res.account_id not in answer:
                answer.append(parse_res.account_id)
        result = main(get_emails, data)
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
                if account.id not in answer:
                    answer.append(account.id)
        db_sess.close()
        return {"accounts_ids": answer}
