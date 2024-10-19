import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Column, Integer, CHAR, ForeignKey


class Groups(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(CHAR)
    users = orm.relationship(
        "Account", back_populates="group", cascade="all, delete-orphan"
    )
