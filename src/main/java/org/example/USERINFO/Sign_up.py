from sqlalchemy import create_engine, insert, select, DateTime
from main.java.org.example.TABLES.tables import Base, Customer
import bcrypt

engine = create_engine('mysql+pymysql://root:toolbox@127.0.0.1:3306/PizzaShop', echo=True)

class signUp:
    def hash_password(password: str) -> str:
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed.decode('utf-8')

    def signUp (full_name:str, username:str, password:str, birthday:str, postal_code:str):
        hashed_password = signUp.hash_password(password)

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


    