import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class ParseResult(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'parse_result'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    text = sqlalchemy.Column(sqlalchemy.Text)
    title = sqlalchemy.Column(sqlalchemy.CHAR)
    timestamp = sqlalchemy.Column(sqlalchemy.Integer)
    url = sqlalchemy.Column(sqlalchemy.CHAR)
    account_post_count = sqlalchemy.Column(sqlalchemy.Integer)
    last_parsing_time = sqlalchemy.Column(sqlalchemy.Integer)
    account_email = sqlalchemy.Column(sqlalchemy.CHAR)
    account_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("accounts.id"))
    account = orm.relationship("Account")
