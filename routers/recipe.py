from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from crud import recipe as recipe_crud
from schemas import recipe as recipe_schema
from config.database import SessionLocal

router = APIRouter(prefix="/recipes", tags=["recipes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[recipe_schema.RecipeOut])
def read_recipes(db: Session = Depends(get_db)):
    recipes = recipe_crud.get_recipes(db)
    print("🔍 Recipes from DB:", recipes)
    return recipes