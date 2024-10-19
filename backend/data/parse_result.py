import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Column, Integer, CHAR, ForeignKey, Text


class ParseResult(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "parse_result"

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(Text)
    title = Column(CHAR)
    timestamp = Column(Integer)
    url = Column(CHAR)
    account_post_count = Column(Integer)
    last_parsing_time = Column(Integer)
    account_email = Column(CHAR)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    account = orm.relationship("Account")
