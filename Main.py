from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import Base, Order, DeliveryPersonnel  # Assuming your models are in 'models.py'
from DeliveryManagement import DeliveryManagement  # Import the separate class

# Database setup
engine = create_engine('mysql+pymysql://root:toolbox@127.0.0.1:3306/PizzaShop', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Initialize database tables (ensure that all the tables exist)
Base.metadata.create_all(engine)

# Create an instance of the DeliveryManagement class
delivery_manager = DeliveryManagement(session)

# Check if delivery personnel are now available
delivery_manager.check_delivery_person_availability()
