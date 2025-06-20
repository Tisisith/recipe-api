from pydantic import BaseModel

class RecipeBase(BaseModel):
    food_name: str
    description: str

class RecipeCreate(RecipeBase):
    pass

class RecipeOut(RecipeBase):
    id: int

    class Config:
        orm_mode = True
