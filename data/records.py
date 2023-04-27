import sqlalchemy
from data.db_session import SqlAlchemyBase


class Record(SqlAlchemyBase):
    __tablename__ = 'records'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    event = sqlalchemy.Column(sqlalchemy.String, nullable=True)
