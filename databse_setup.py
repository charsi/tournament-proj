import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()


class Restaurant(Base):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg
  
class Menuitem(Base):
    """docstring for Menuitem"""
    def __init__(self, arg):
        super(Menuitem, self).__init__()
        self.arg = arg
        


name = Column(String(80), nullable = False)

id = Column(String(250))




engine = create_engine(
    'sqlite://restaurantmenu.db')


Base.metadata.create_all()
