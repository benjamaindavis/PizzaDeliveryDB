from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.types import Boolean
from decimal import Decimal
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine('mysql+pymysql://root:toolbox@127.0.0.1:3306/PizzaShop', echo=True)

class Customers(Base): # DROP TABLE IF EXISTS, use later if new column is needed
    __tablename__ = 'customers'
    
    customer_id = Column(Integer, primary_key = True, autoincrement = True)
    full_name = Column(String(50))# identification...
    username = Column(String(50), unique = True)# login info
    password = Column(String(100))# LONGER FOR HASHING
    birthday = Column(DateTime) # for discounts
    pizza_count = Column(Integer) # for discounts
    postal_code = Column(String(10)) # for data ig...
    #add pizza_count code, make null if nothign is in there


class Discount(Base):
    __tablename__ = 'discounts'

    discount_id = Column(Integer, primary_key = True, autoincrement = True)
    discount_code = Column(Integer)
    discount_type = Column(String(10))
    discount_used = Column(Boolean)

class Pizza(Base):
    __tablename__ = 'pizza'

    pizza_id = Column(Integer, primary_key = True, autoincrement = True)
    pizza_name = Column(String(50))
    pizza_price = Column(Decimal(5,2))
    vegetarian = Column(Boolean)
    vegan = Column(Boolean)

class Drinks(Base):
    __tablename__ = 'drinks'

    drink_id = Column(Integer, primary_key = True, autoincrement = True)
    drink_type = Column(String(50), unique = True)
    drink_cost = Column(Decimal(5,2))

class Desserts(Base):
    __tablename__ = 'desserts'

    dessert_id = Column(Integer, primary_key = True, autoincrement = True)
    dessert_type = Column(String(50), unique = True)
    dessert_cost = Column(Decimal(5,2))

class Ingredients(Base):
    __tablename__ = 'ingredients'

    ingredient_id = Column(Integer, primary_key = True, autoincrement = True)
    ingredient_name = Column(String(50))
    ingredient_cost = Column(Decimal(5,2))
    vegetarian = Column(Boolean)
    vegan = Column(Boolean)

class Order(Base):
    __tablename__ = 'order'

    order_id = Column(Integer, primary_key = True, autoincrement = True)
    order_total = Column(Decimal(7,2))
    delivery_address = Column(String(50))
    #cancel_time = Column()
    delivery_time_minutes = Column(Integer)

            














Base.metadata.create_all(engine)
