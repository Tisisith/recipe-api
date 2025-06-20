from sqlalchemy.orm import Session
from models.recipe import Recipe
from schemas.recipe import RecipeCreate

def get_recipes(db: Session):
    return db.query(Recipe).all()
