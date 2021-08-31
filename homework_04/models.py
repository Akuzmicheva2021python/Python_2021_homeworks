"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import asyncio
import os
from asyncio import current_task
from sqlalchemy import ForeignKey
from sqlalchemy import MetaData, Column, Integer, String, Boolean, Text
from sqlalchemy.ext.asyncio import async_scoped_session
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

# Base = None
# Session = None

engine = create_async_engine(
        PG_CONN_URI,
        # echo=True,
        )

metadata_obj = MetaData(bind=engine, schema='lesson')

Base = declarative_base(bind=engine, metadata=metadata_obj)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False)
    name = Column(String(50), nullable=False, default='', server_default='')
    deleted = Column(Boolean, nullable=False, default=False, server_default='False')
    # отношение один-к-многим с двунаправленными связями
    # children = relationship("Child" [, back_populates="parent"])
    posts = relationship('Post', back_populates='user')
    __mapper_args__ = {"eager_defaults": True}

    def __init__(self, username, email, name=''):
        self.username = username
        self.email = email
        self.name = name

    def __repr__(self):
        return f"{self.__class__.__name__} : (id={self.id!r}, username={self.username!r}, " \
               f"email={self.email!r}, name={self.name!r} )"


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, default='Lesson04', server_default='Lesson04')
    body = Column(Text, nullable=False, default='', server_default='')
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    # отношение один-к-многим с двунаправленными связями
    # parents = relationship("Parent", back_populates="children")
    user = relationship('User', back_populates='posts')
    __mapper_args__ = {"eager_defaults": True}

    def __init__(self, title, body, user_id):
        self.title = title
        self.body = body
        self.user_id = user_id

    def __repr__(self):
        return f'{self.__class__.__name__} : id={self.id!r}, ' \
               f'user_id = {self.user_id}, title = {self.title!r}'


async_session_factory = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)


Session = async_scoped_session(async_session_factory, scopefunc=current_task)
