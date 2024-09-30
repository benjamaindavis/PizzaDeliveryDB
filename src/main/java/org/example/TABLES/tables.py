from sqlalchemy import Column, Integer, String, DateTime, create_engine, ForeignKey
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
    pizza_discount_code = Column(String(10), nullable = True)


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
    customer_id = Column(Integer, ForeignKey('customer.customer_id'))
    order_total = Column(Decimal(7,2))
    delivery_address = Column(String(50))
    cancel_time = Column(Boolean) # bool for ease of checking if the customer wants to cancel (5 min limit)
    delivery_time_minutes = Column(Integer)

class OrderPizza(Base):
    __tablename__ = 'orderpizza'

    order_id = Column(Integer, ForeignKey('order.order_id'), primary_key=True, autoincrement=True)
    pizza_id = Column(Integer, ForeignKey('pizza.pizza_id'), primary_key=True, autoincrement=True)
    pizza_amount = Column(Integer)

class OrderDrink(Base):
    __tablename__ = 'orderdrink'

    order_id = Column(Integer, ForeignKey('order.order_id'), primary_key=True, autoincrement=True)
    drink_id = Column(Integer, ForeignKey('drink.drink_id'), primary_key=True, autoincrement=True)
    drink_amount = Column(Integer)

class OrderDessert(Base):
    __tablename__ = 'orderdessert'

    order_id = Column(Integer, ForeignKey('order.order_id'), primary_key=True, autoincrement=True)
    dessert_id = Column(Integer, ForeignKey('dessert.dessert_id'), primary_key=True, autoincrement=True)
    dessert_amount = Column(Integer)

class PizzaIngredients(Base):
    __tablename__ = 'pizzaingredients'

    pizza_id = Column(Integer, ForeignKey('pizza.pizza_id'), primary_key=True, autoincrement=True)
    ingredients_id = Column(Integer, ForeignKey('ingredients.ingredients_id'), primary_key=True, autoincrement=True)

class DeliveryPersonnel(Base):
    __tablename__ = 'delivery_personnel'

    personnel_id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(50), nullable=False)
    postal_code_assigned = Column(String(10), nullable=False)  # Assigned area of delivery
    is_available = Column(Boolean, default=True)  # Whether the person is available for delivery
    next_available_time = Column(DateTime, nullable=True)  # When they'll be available next


#ADDING STUFF INTO THE TABLES
#----------------------------



            














Base.metadata.create_all(engine)
