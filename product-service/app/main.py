from fastapi import FastAPI
from app.routes.product_routes import router
from app.database.connection import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)