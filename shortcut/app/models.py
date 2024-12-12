import json

from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey, Text

from app.extensions import Base
from app.settings import Settings

settings = Settings()


class Category(Base):
    __tablename__ = 'category'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    type = Column('type', String(10))
    name = Column('name', String(60))
    desc = Column('desc', String(300), default='')
    shortcuts = relationship('Shortcut', back_populates='category')


class Shortcut(Base):
    __tablename__ = 'shortcut'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    tag = Column('tag', String(100), default='')
    type = Column('type', String(10), default='单键')
    content = Column('content', Text, default='{}')
    conflict = Column('conflict', Text, default='{}')
    function = Column('function', String(100), default='')
    function_en = Column('function_en', String(100), default='')
    category_id = Column('category_id', Integer, ForeignKey('category.id'))
    category = relationship('Category', back_populates='shortcuts')


class Keys(Base):
    __tablename__ = 'keys'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    id_ = Column('id_', Integer, unique=True)
    type = Column(String(20))
    name1 = Column(String(20))
    name2 = Column(String(20))


class Mouse(Base):
    __tablename__ = 'mouse'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    id_ = Column('id_', Integer, unique=True)
    name = Column(String(30), unique=True)
