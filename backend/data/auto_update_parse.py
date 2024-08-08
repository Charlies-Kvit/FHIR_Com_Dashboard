from . import db_session
from .account import Account
from .parse_result import ParseResult
from parsing.main_parse import main
import time


def update():
    db_sess = db_session.create_session()
    accounts = db_sess.query(Account).all()
    emails = [account.email for account in accounts]
    result = main(emails)
    for email in emails:
        if email not in result:
            continue
        parse_results = db_sess.query(ParseResult).filter(ParseResult.account_email == email).all()
        for parse_result in parse_results:
            db_sess.delete(parse_result)
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
