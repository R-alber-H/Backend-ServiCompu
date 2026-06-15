from fastapi import FastAPI
from app.database import engine, Base
import app.models
from app.routers import auth,users

app = FastAPI(title="ServiCompu API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Cyber API funcionando"}
app.include_router(auth.router)
app.include_router(users.router)