from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"

    email = Column(String, primary_key=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    todo_items = relationship("Todo", back_populates="owner")
    post_items = relationship("Post", back_populates="owner")


class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String, index=True)
    esg = Column(String, index=True)
    timestamp = Column(Integer, index=True)
    owner_email = Column(Integer, ForeignKey("users.email"))

    owner = relationship("User", back_populates="items")


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String, index=True)
    esg = Column(String, index=True)
    timestamp = Column(Integer, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
