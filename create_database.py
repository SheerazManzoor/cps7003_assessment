from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    address = Column(String)


class Employee(Base):
    __tablename__ = 'employees'
    employee_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    position = Column(String)
    email = Column(String)
    phone_number = Column(String)


class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    category = Column(String)
    price = Column(Integer)
    stock_quantity = Column(Integer)
    order = relationship('Order', back_populates='product', uselist=False)


class Order(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    product_id = Column(Integer, ForeignKey('products.product_id'))
    employee_id = Column(Integer, ForeignKey('employees.employee_id'))
    order_date = Column(DateTime, default=datetime.utcnow)
    quantity = Column(Integer)
    product = relationship('Product', back_populates='order')


class PurchaseHistory(Base):
    __tablename__ = 'purchase_histories'
    purchase_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    product_id = Column(Integer, ForeignKey('products.product_id'))
    purchase_date = Column(String)
    price = Column(Integer)
    quantity = Column(Integer)


class CommunicationLog(Base):
    __tablename__ = 'communication_logs'
    log_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    timestamp = Column(String)
    communication_type = Column(String)
    communication_content = Column(String)


def create_database():
    engine = create_engine('sqlite:///my_database.db')
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    return sessionmaker(bind=engine)
