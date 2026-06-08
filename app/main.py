from fastapi import FastAPI
from app.database import engine, Base
import app.models
from app.routers import auth

app = FastAPI(title="ServiCompu API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "ServiCompu API funcionando"}
app.include_router(auth.router)