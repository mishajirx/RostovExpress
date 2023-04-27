import sqlalchemy
from data.db_session import SqlAlchemyBase


class Order(SqlAlchemyBase):
    __tablename__ = 'orders'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    weight = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    region = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    orders_courier = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('couriers.id'))
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    complete_time = sqlalchemy.Column(sqlalchemy.String, nullable=True, default='')

    sqlalchemy.orm.relation('User')
    sqlalchemy.orm.relation('Courier')
