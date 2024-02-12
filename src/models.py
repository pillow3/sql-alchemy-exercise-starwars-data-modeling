import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class FavoriteItem(Base):
    __tablename__ = 'favorite_items'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True, nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=True)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    favorites = relationship('FavoriteItem', back_populates='user')

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    diameter = Column(String(250), nullable=True)
    name = Column(String(250), nullable=True)
    diameter = Column(Float)
    population = Column(Integer)

    favorite_id = relationship('FavoriteItem', backref='planets')

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    last_name = Column(String(250))
    height = Column(Float)

    favorite_id = relationship('FavoriteItem', backref='characters')



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
