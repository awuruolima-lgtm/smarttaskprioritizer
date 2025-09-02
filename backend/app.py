# backend/app.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud, db, prioritizer
from fastapi import FastAPI
from .db import engine, Base
from .routers import prioritize

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Task Prioritizer API")

# Include routers
app.include_router(prioritize.router)

@app.get("/")
def root():
    return {"message": "Welcome to Smart Task Prioritizer API"}

