from sqlalchemy.orm import Session
from models.recipe import Recipe, Ingredient, RecipeIngredient, Instruction
from schemas.recipe import RecipeCreate

def get_recipes(db: Session):
    return db.query(Recipe).all()

def get_recipe_by_id(db: Session, recipe_id: int):
    return db.query(Recipe).filter(Recipe.id == recipe_id).first()

def create_recipe(db: Session, recipe: RecipeCreate):
    db_recipe = Recipe(
        recipe_name=recipe.recipe_name,
        image_url=recipe.image_url,
        short_description=recipe.short_description
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)

    for ing in recipe.ingredients:
        db_ing = db.query(Ingredient).filter(Ingredient.name == ing.name).first()
        if not db_ing:
            db_ing = Ingredient(name=ing.name)
            db.add(db_ing)
            db.commit()
            db.refresh(db_ing)

        db_link = RecipeIngredient(recipe_id=db_recipe.id, ingredient_id=db_ing.id)
        db.add(db_link)

    for inst in recipe.instructions:
        db_inst = Instruction(recipe_id=db_recipe.id, step_name=inst.name)
        db.add(db_inst)

    db.commit()
    return db_recipe