from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas import recipe as schema
from controllers.recipe_controller import read_recipes, read_recipe, add_recipe
from utils.dependencies import get_db

router = APIRouter(prefix="/recipes", tags=["recipes"])

@router.get("/", response_model=List[schema.RecipeOut])
def get_recipes(db: Session = Depends(get_db)):
    return read_recipes(db)

@router.get("/{recipe_id}", response_model=schema.RecipeOut)
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return read_recipe(recipe_id, db)

@router.post("/", response_model=schema.RecipeOut)
def create_recipe(recipe: schema.RecipeCreate, db: Session = Depends(get_db)):
    return add_recipe(db, recipe)