from fastapi import FastAPI
from post_library_summary import router as library_upload_router
from models import BookData
app = FastAPI()

app.include_router(library_upload_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}