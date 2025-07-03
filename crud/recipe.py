from sqlalchemy.orm import Session
from models.recipe import Recipe
from schemas.recipe import RecipeCreate

def get_recipes(db: Session):
    return db.query(Recipe).all()

def get_recipe_by_id(db: Session, recipe_id: int):
    return db.query(Recipe).filter(Recipe.id == recipe_id).first()