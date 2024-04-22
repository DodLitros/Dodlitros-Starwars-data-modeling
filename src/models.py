import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250),  nullable=False)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    favorites = relationship("Favorites", back_populates="user")

class Favorites(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    item_name = Column(String(250), nullable=False)
    item_id = Column(String(250), nullable=False)
    user = relationship("User", back_populates="favorites")

class People(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    height = Column(Float, nullable=False)
    mass = Column(Float, nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    films_id = Column(Integer, ForeignKey("films.id"))

class Planets(Base):
    __tablename__ = "planets"

    id=Column(Integer, primary_key=True, nullable=False)
    diameter= Column(Integer, nullable=False)
    rotation_period= Column(Integer, nullable=False)
    orbital_period= Column(Integer, nullable=False)
    population= Column(Integer, nullable=False)
    gravity= Column(String(250), nullable=False)
    climate= Column(String(250), nullable=False)
    terrain= Column(String(250), nullable=False)
    surface_water= Column(Float, nullable=False)
    created= Column(String(250), nullable=False)
    edited= Column(String(250), nullable=False)
    url= Column(String(250), nullable=False)
    films_id = Column(Integer, ForeignKey("films.id"), nullable=False)
    people = relationship("People", backref="planets")

class Films(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True, nullable=False)
    characters = Column(String(250), nullable=False)
    planets = Column(String(250), nullable=False)
    starships = Column(String(250), nullable=False)
    vehicles = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)
    created = Column(String)
    edited = Column(String(250))
    producer= Column(String(100), nullable=False)
    title = Column(String(250), nullable=False)
    episode_id=Column(Integer, nullable=False)
    director= Column(String(250), nullable=False)
    release_date= Column(String(250), nullable=False)
    opening_crawl= Column(String(5000), nullable=False)
    url= Column(String(250), nullable=False)
    planets = relationship("Planets", backref="films")
    people = relationship("People", secondary="cast")

class Cast(Base):
    __tablename__ ="cast"
    
    id = Column(Integer, primary_key=True, nullable=False)
    film_id=Column(Integer, ForeignKey("films.id"))
    film=relationship("Films", backref="cast")
    people_id=Column(Integer, ForeignKey("people.id"))
    people= relationship("People", backref="cast")
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

