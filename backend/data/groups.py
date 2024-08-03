import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Groups(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "groups"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.CHAR)
    users = orm.relationship("Account", back_populates='group', cascade="all, delete-orphan")

