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
    user_post_count = sqlalchemy.Column(sqlalchemy.Integer)
    last_parsing_time = sqlalchemy.Column(sqlalchemy.Integer)
    user_email = sqlalchemy.Column(sqlalchemy.CHAR, sqlalchemy.ForeignKey("users.email"))
    user = orm.relationship("User")
