from sqlalchemy import Column, Integer, String
from config.database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    food_name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
