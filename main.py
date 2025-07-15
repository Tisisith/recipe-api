from fastapi import FastAPI
from routers import recipe as recipe_router
from config.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(recipe_router.router)
