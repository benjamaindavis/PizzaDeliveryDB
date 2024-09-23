from sqlalchemy import create_engine, Column, Integer, String, Date, insert, delete, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine('mysql+pymysql://root:toolbox@127.0.0.1:3306/PizzaShop', echo=True)

class Customer(Base): # DROP TABLE IF EXISTS, use later if new column is needed
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key = True, autoincrement = True)
    full_name = Column(String(50))# identification...
    username = Column(String(50), unique = True)# login info
    password = Column(String(50))# login info
    birthday = Column(DateTime) # for discounts
    pizza_count = Column(Integer) # for discounts
    postal_code = Column(String(10)) # for data ig...



def insertCustomer (full_name:String, username:String, password:String, birthday:String, postal_code:String):
    #add pass_hash later

    #birthday_date = DateTime.strptime(birthday, '%Y-%m-%d').date()


    with engine.connect() as conn:
        conn.execute(insert(Customer).values(full_name = full_name, username = username, password = password, birthday = birthday, pizza_count = 0, postal_code = postal_code))
        
        conn.commit()

















Base.metadata.create_all(engine)

#print(repr(User.__table__)) use this for debugging