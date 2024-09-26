from sqlalchemy import create_engine, insert, select, DateTime, update
from main.java.org.example.TABLES.tables import Base, Customers, Order, Drinks, Desserts, Pizza
from datetime import datetime
from decimal import Decimal
import random, string

engine = create_engine('mysql+pymysql://root:toolbox@127.0.0.1:3306/PizzaShop', echo=True)

def generate_discount_code(length = 10) -> str: # add a discount code delete functio nthat checks if the discount code is used bt the person
    characters = string.ascii_uppercase + string.digits
    discount_code = ''.join(random.choice(characters)for _ in range(length))
    return discount_code

def code_validity_checker():
    pass

def check_birthday(customer_id: int) -> bool:
    with engine.connect() as conn:

        todays_date = datetime.today().date()

        birthday_check = conn.execute(
            select(Customers).where(Customers.customer_id == customer_id)
        ).fetchone()

        if birthday_check and birthday_check.birthday.date() == todays_date:
            return True
        else:
            return False

def check_pizza_count(customer_id: int) -> bool:
    with engine.connect() as conn:

        pizza_count_check = conn.execute(
            select(Customers).where(Customers.customer_id == customer_id)
        ).fetchone()

        if pizza_count_check:
            pizza_count = pizza_count_check.pizza_count

            return pizza_count % 10 == 0
        
    return False

def applyBirthdayDiscount(order_id: int, customer_id: int) -> Decimal:
    with engine.connect() as conn:
        
        if check_birthday(customer_id):
            
            order = conn.execute(
                select(Order).where(Order.order_id == order_id)
            ).fetchone()

            if order:
                current_total = order.order_total

                # Fetch the price of the default pizza and drink
                pizza = conn.execute(
                    select(Pizza).where(Pizza.pizza_name == DEFAULT_PIZZA_NAME) # FIGURE OUT WHAT TO DOOOOO
                ).fetchone()

                drink = conn.execute(
                    select(Drinks).where(Drinks.drink_type == DEFAULT_DRINK_TYPE)# :(
                ).fetchone()

                if pizza and drink:
                    pizza_price = pizza.pizza_price
                    drink_price = drink.drink_cost

                    discount_amount = pizza_price + drink_price
                    new_total = current_total - discount_amount

                    conn.execute(
                        update(Order).where(Order.order_id == order_id).values(order_total = new_total)
                    )
                    conn.commit()  

                    return new_total

    # If no discount is applied, return the original total (or handle as needed)
    return current_total if order else Decimal('0.00')  # or raise an exception, etc.

def applyPizzaCountDiscount():
    pass

#Base.metadata.create_all(engine)