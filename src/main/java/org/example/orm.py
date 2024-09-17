from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:toolbox@127.0.0.1:3306/PizzaShop', echo=True)

from sqlalchemy.orm import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, Date

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key = True, autoincrement = True)
    full_name = Column(String(50))# identification...
    username = Column(String(50))# login info
    password = Column(String(50))# login info
    birthday = Column(Date) # for discounts
    pizza_count = Column(Integer) # for discounts

    def __repr__(self):
        return "<User(full_name='%s', username='%s', password='%s', birthday='%d', pizza_count='%i')>" % (
        self.name, self.username, self.password, self.birthday, self.pizza_count)


#Base.metadata.create_all(engine)

#print(repr(User.__table__))