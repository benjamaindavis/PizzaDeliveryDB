from sqlalchemy import create_engine, insert, select, DateTime
from tables import Base, Customer
import bcrypt

engine = create_engine('mysql+pymysql://root:toolbox@127.0.0.1:3306/PizzaShop', echo=True)

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

def generate_discount_code() -> int:
    

def check_birthday(birthday:DateTime):
    with engine.connect() as conn:

        birthday_check = conn.execute(
            select(Customer).where(Customer.birthday == THE CURRENT DATE)
        ).fetchone()

        if birthday_check:





#Base.metadata.create_all(engine)