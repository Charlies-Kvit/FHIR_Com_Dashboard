from . import db_session
import time
from flask_restful import abort, Resource, reqparse
from .parse_result import ParseResult
from flask import request
from parsing.main_parse import main


parser = reqparse.RequestParser()
parser.add_argument("emails")


class ParseRequestResource(Resource):
    def post(self):
        args = parser.parse_args()
        emails = args["emails"]
        """start_time = args["start_time"]
        end_time = args["end_time"]"""
        get_emails = []
        do_emails = []
        db_sess = db_session.create_session()
        for email in emails:
            parse_res = db_sess.query(ParseResult).filter(ParseResult.user_email == email).first()
            if not parse_res:
                get_emails.append(email)
                continue
            do_emails.append(email)
        result = main(get_emails)
        for email in get_emails:
            for el in result[email]:
                parse_result = ParseResult(
                    text=el["text"],
                    title=el["title"],
                    timestamp=int(el["timestamp"]),
                    last_parsing_time=time.time(),
                    user_email=email,
                    user_post_count=el["count"],
                    url=el["url"]
                )
                db_sess.add(parse_result)
                db_sess.commit()
        answer = {}
        for email in emails:
            email_parse_res = db_sess.query(ParseResult).filter(
                ParseResult.user_email == email
            ).all()
            answer[email] = [parse_res.to_dict(only=("id", "title", "url", "user_post_count", "text"))
                             for parse_res in email_parse_res]
        return answer
