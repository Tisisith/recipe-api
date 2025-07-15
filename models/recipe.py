from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    recipe_name = Column(String(255))
    image_url = Column(Text)
    short_description = Column(Text)

    ingredients_link = relationship("RecipeIngredient", back_populates="recipe", cascade="all, delete-orphan")
    ingredients = relationship("Ingredient", secondary="recipe_ingredients", lazy="subquery")
    instructions = relationship("Instruction", back_populates="recipe", cascade="all, delete-orphan")

class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True)

    recipe_links = relationship("RecipeIngredient", back_populates="ingredient", cascade="all, delete-orphan")

class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredients"

    id = Column(Integer, primary_key=True, index=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"))

    recipe = relationship("Recipe", back_populates="ingredients_link")
    ingredient = relationship("Ingredient", back_populates="recipe_links")

class Instruction(Base):
    __tablename__ = "instructions"

    id = Column(Integer, primary_key=True, index=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    step_name = Column(Text)

    recipe = relationship("Recipe", back_populates="instructions")