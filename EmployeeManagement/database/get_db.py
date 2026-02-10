from .config_db import Base, engine, session
from sqlalchemy import Column, Integer, String, Boolean, Float

class Employee(Base):
    __tablename__ = "EMPLOYEE"
    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String, nullable = False)
    email = Column(String(50), unique = True, nullable = False)
    department = Column(String, nullable = False)
    salary = Column(Float, nullable = False)
    phone_number = Column(String(10), unique = True, nullable = False)
    is_active = Column(Boolean, nullable = False, default = True)

def create_tables():
    try:
        Base.metadata.create_all(engine)
        print("Tables Created Successfully")
    except Exception as e:
        print("Tables Creation Failed", e)

def get_db():
    db = session
    try:
        yield db
    finally:
        db.close()