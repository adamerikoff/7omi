from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

import bcrypt


Base = declarative_base()

class User(Base):
  __tablename__ = 'users'
  user_id = Column(Integer, primary_key=True)
  username = Column(String(255), nullable=False, unique=True)
  password = Column(String(255), nullable=False)

  def __repr__(self) -> str:
    """Returns string representation of model instance"""
    return "<User {full_name!r}>".format(full_name=f"{self.user_id} {self.username}")
  
  @staticmethod
  def hash_password(password) -> str:
    """Transforms password from it's raw textual form to 
    cryptographic hashes
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
