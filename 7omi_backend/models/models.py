from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import relationship

from db import Base, engine

import bcrypt

class User(Base):
  __tablename__ = 'users'
  user_id = Column(Integer, primary_key=True)
  username = Column(String(255), nullable=False, unique=True)
  password = Column(String(255), nullable=False)

  # conversations = relationship('Conversation', secondary='user_conversation', back_populates='user')

  @staticmethod
  def hash_password(password) -> str:
    """Transforms password from it's raw textual form to 
    cryptographic hashes
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
  
class Conversation(Base):
  __tablename__ = 'conversations'
  conversation_id = Column(Integer, primary_key=True)
  name = Column(String(255), nullable=False)

  # users = relationship('User', secondary='user_conversation', back_populates='conversations')
  # messages = relationship('Message', back_populates='conversation')

class UserConversation(Base):
  __tablename__ = 'user_conversation'
  user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
  conversation_id = Column(Integer, ForeignKey('conversations.conversation_id'), primary_key=True)

class Message(Base):
  __tablename__ = 'messages'
  message_id = Column(Integer, primary_key=True)
  content = Column(String)
  user_id = Column(Integer, ForeignKey('users.user_id'))
  conversation_id = Column(Integer, ForeignKey('conversations.conversation_id'))
  # Define relationship to user
  # user = relationship('User', back_populates='messages')
  # Define relationship to conversation
  # conversation = relationship('Conversation', back_populates='messages')

Base.metadata.create_all(engine)
