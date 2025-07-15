from crud.recipe import get_recipes, get_recipe_by_id, create_recipe
from schemas.recipe import RecipeCreate

def read_recipes(db):
    return get_recipes(db)

def read_recipe(recipe_id, db):
    return get_recipe_by_id(db, recipe_id)

def add_recipe(db, recipe: RecipeCreate):
    return create_recipe(db, recipe)