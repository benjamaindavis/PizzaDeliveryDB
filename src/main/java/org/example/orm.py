from sqlalchemy import create_engine, Column, Integer, String, insert, DateTime, select
from sqlalchemy.types import Boolean
from decimal import Decimal
from sqlalchemy.orm import declarative_base
import bcrypt

Base = declarative_base()
engine = create_engine('mysql+pymysql://root:toolbox@127.0.0.1:3306/PizzaShop', echo=True)

class Customer(Base): # DROP TABLE IF EXISTS, use later if new column is needed
    __tablename__ = 'customers'
    
    customer_id = Column(Integer, primary_key = True, autoincrement = True)
    full_name = Column(String(50))# identification...
    username = Column(String(50), unique = True)# login info
    password = Column(String(100))# LONGER FOR HASHING
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
# everything above is table creation
#-----------------------------------------------------------------------------------------------------------------------
# below are functions for the logic

def hash_password(password: str) -> str:
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed.decode('utf-8')

def signUp (full_name:str, username:str, password:str, birthday:str, postal_code:str):
    hashed_password = hash_password(password)

    with engine.connect() as conn:
        
        existing_user = conn.execute(
            select(Customer).where(Customer.username == username)
        ).fetchone()

        if existing_user:
            print("Username is taken!")
            return None

        # insert new customer
        conn.execute(insert(Customer).values(
            full_name = full_name,
            username = username,
            password = hashed_password,
            birthday = birthday,
            pizza_count = 0 ,  
            postal_code = postal_code
            )
        )

        conn.commit()
        print("Signup successful!")

def verify_password(user_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password.encode('utf-8'))


def login(username:str, password:str):
     with engine.connect() as conn:
        #fetch user by username
        user_record = conn.execute(
            select(Customer).where(Customer.username == username)
        ).fetchone()

        if user_record:
            if verify_password(password, user_record.password):
                print("Login successful!")
                return user_record 
            else:
                print("Invalid password!")
                return None
        else:
            print("User not found! Please create an account!")
            return None

#def applyDiscount(user, order):















#Base.metadata.create_all(engine)
