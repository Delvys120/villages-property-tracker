from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Property(Base):
    __tablename__ = 'properties'

    id = Column(Integer, primary_key=True)
    address = Column(String)
    price = Column(Float)
    bedrooms = Column(Integer)
    bathrooms = Column(Float)
    sqft = Column(Integer)
    listing_date = Column(DateTime)
    # Add more fields as needed

class DatabaseManager:
    def __init__(self, db_url='sqlite:///villages_properties.db'):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add_property(self, property_data):
        session = self.Session()
        try:
            new_property = Property(**property_data)
            session.add(new_property)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error adding property: {e}")
        finally:
            session.close()