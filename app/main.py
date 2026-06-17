from fastapi import FastAPI
from app.database import engine, Base
import app.models
from app.routers import auth,users,products,brand,category,supplier
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ServiCompu API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Cyber API funcionando"}
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(products.router)
app.include_router(brand.router)
app.include_router(category.router)
app.include_router(supplier.router)