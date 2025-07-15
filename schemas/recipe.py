from pydantic import BaseModel, Field
from typing import List

class IngredientBase(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class InstructionBase(BaseModel):
    id: int
    name: str = Field(..., alias='step_name')

    class Config:
        from_attributes = True
        validate_by_name = True

class IngredientCreate(BaseModel):
    name: str

class InstructionCreate(BaseModel):
    name: str

class RecipeBase(BaseModel):
    recipe_name: str
    image_url: str
    short_description: str

class RecipeCreate(RecipeBase):
    ingredients: List[IngredientCreate]
    instructions: List[InstructionCreate]

class RecipeOut(RecipeBase):
    id: int
    ingredients: List[IngredientBase]
    instructions: List[InstructionBase]

    class Config:
        from_attributes = True