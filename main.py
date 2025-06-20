from fastapi import FastAPI
from routers import recipe  # 🔁 changed from 'app.routers'

from config.database import engine
from models import recipe as recipe_model

recipe_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(recipe.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Recipe API!"}