from fastapi import FastAPI
from src.rotas.rotas import rotas
from src.database.settings.entities import load_tables

load_tables()

app = FastAPI()
app.include_router(rotas)
