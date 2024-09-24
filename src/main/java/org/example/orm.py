from sqlalchemy import create_engine, Column, Integer, String, insert, DateTime
from sqlalchemy.types import Boolean
from decimal import Decimal
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine('mysql+pymysql://root:toolbox@127.0.0.1:3306/PizzaShop', echo=True)

class Customer(Base): # DROP TABLE IF EXISTS, use later if new column is needed
    __tablename__ = 'customers'
    
    customer_id = Column(Integer, primary_key = True, autoincrement = True)
    full_name = Column(String(50))# identification...
    username = Column(String(50), unique = True)# login info
    password = Column(String(50))# login info
    birthday = Column(DateTime) # for discounts
    pizza_count = Column(Integer) # for discounts
    postal_code = Column(String(10)) # for data ig...

class Discount(Base):
    __tablename__ = 'discounts'

    discount_id = Column(Integer, primary_key = True, autoincrement = True)
    discount_code = Column(Integer)
    discount_type = Column(String(10))

class Pizza(Base):
    __tablename__ = 'pizza'

    pizza_id = Column(Integer, primary_key = True, autoincrement = True)
    pizza_name = Column(String(50))
    pizza_price = Column(Decimal(5,2))
    vegetarian = Column(Boolean)
    vegan = Column(Boolean)

class Ingredients(Base):
    __tablename__ = 'ingredients'

    ingredient_id = Column(Integer, primary_key = True, autoincrement = True)
    ingredient_name = Column(String(50))
    ingredient_cost = Column(Decimal(5,2))
    vegetarian = Column(Boolean)
    vegan = Column(Boolean)

class Order(Base):
    __tablename__ = 'order'



def insertCustomer (full_name:String, username:String, password:String, birthday:String, postal_code:String):
    #add pass_hash later

    with engine.connect() as conn:
        conn.execute(insert(Customer).values(full_name = full_name, username = username, password = password, birthday = birthday, pizza_count = 0, postal_code = postal_code))
        
        conn.commit()

def applyDiscount(order):


















Base.metadata.create_all(engine)

#print(repr(User.__table__)) use this for debugging