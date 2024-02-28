from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_config = {
  "dialect": "postgresql",
  "engine": "psycopg2",
  "user": "postgres",
  "password": "postgres",
  "host": "localhost",
  "port": "5432",
  "database": "7omi"
}
SQLALCHEMY_DATABASE_URL = f"{db_config['dialect']}+{db_config['engine']}://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
