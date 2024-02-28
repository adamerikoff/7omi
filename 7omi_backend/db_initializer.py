
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# for postgreSQL database credentials can be written as 
user = 'postgres'
password = 'postgres'
host = 'localhost'
port = '5432'
database = '7omi'
# for creating connection string
connection_str = f"postgresql:// {user}:{password}@{host}:{port}/{database}"
# SQLAlchemy engine

# Create database engine
engine = create_engine(connection_str, echo=True, future=True)

# Create database declarative base
Base = declarative_base()

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
  """Database session generator"""
  db = SessionLocal()
  try:
      yield db
  finally:
      db.close()