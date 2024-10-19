from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Column, Integer, CHAR, ForeignKey


class Account(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    zulip_id = Column(Integer)
    name = Column(CHAR)
    email = Column(CHAR)
    avatar_url = Column(CHAR)
    group_id = Column(Integer, ForeignKey("groups.id"))
    parse_results = orm.relationship("ParseResult", back_populates="account")
    group = orm.relationship("Groups")
