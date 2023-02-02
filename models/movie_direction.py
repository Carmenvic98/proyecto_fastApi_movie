from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base

class Movie_direction(Base):

    __tablename__="movie_direction"
    dir_id = Column(Integer, ForeignKey("director.id"))
    movie_id = Column(Integer, ForeignKey("movie.id"))