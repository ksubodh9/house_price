# main.py

from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine
from routes import items
from db import engine
from routes import predict_house

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}


app.include_router(items.router, prefix="/items")
app.include_router(predict_house.router, prefix="/ml", tags=["HousePricePredictor"])

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)