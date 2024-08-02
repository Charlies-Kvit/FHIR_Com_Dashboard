import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin


class Account(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'accounts'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.CHAR)
    email = sqlalchemy.Column(sqlalchemy.CHAR)
    avatar_url = sqlalchemy.Column(sqlalchemy.CHAR)
    group_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("groups.id"))
    parse_results = orm.relationship("ParseResult", back_populates='account')
    group = orm.relationship('Groups')

