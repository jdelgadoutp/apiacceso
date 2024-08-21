from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database_url = f"postgresql+psycopg2://postgres:kyndo.net@localhost:5432/acceso"

engine = create_engine(database_url, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()