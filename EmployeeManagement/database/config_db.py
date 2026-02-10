import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_CONNECTION_URL = os.getenv("DATABASE_CONNECTION_URL")

try:
    engine = create_engine(DATABASE_CONNECTION_URL)
    print("Connection Successful")

    Base = declarative_base()

    Session = sessionmaker(bind = engine)
    session = Session()
    print("Session Initialized Successful")
except ConnectionError as err:
    print("Connection Error")
except Exception as e:
    print(e)