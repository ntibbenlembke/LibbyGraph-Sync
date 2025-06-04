from fastapi import FastAPI
from post_library_summary import router as library_upload_router
from models import BookData
from database import engine
import db_models

db_models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="LibbyGraph API", 
              description="API for managing library book data")

app.include_router(library_upload_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the LibbyGraph API"}