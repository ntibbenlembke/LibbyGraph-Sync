from fastapi import APIRouter, UploadFile, File, Body
import pandas as pd
from io import StringIO, BytesIO
from models import BookData, LibraryResponse
from fastapi.responses import JSONResponse
from fastapi import status
from typing import List

router = APIRouter(prefix="/library", tags=["library"])

@router.get("/upload/")
async def get_library_summary():
    return {"message": "Welcome to the library summary API"}

@router.post("/upload/", 
             response_model=LibraryResponse,
             summary="Upload a CSV file with book data",
             description="Upload a CSV file containing library book data and get it converted to JSON format.",
             response_description="The parsed book data in JSON format")
async def upload_csv(file: UploadFile = File(...)):
    """
    Upload a CSV file with book data and convert it to JSON.
    
    The CSV file should have the following columns:
    - Title (required)
    - Authors (required)
    - Contributors
    - ISBN/UID
    - Format
    - Read Status
    - Date Added
    - etc.
    
    Returns a JSON object with the parsed data.
    """
    try:
        # read the file
        contents = await file.read()
        df = pd.read_csv(BytesIO(contents))
        
        # convert to lowercase to match json
        df.columns = [col.lower() for col in df.columns]
        
        df = df.replace({pd.NA: None, float('nan'): None})
        
        # Convert numeric columns that should be strings to strings
        if 'isbn/uid' in df.columns:
            df['isbn/uid'] = df['isbn/uid'].astype(str)
        
        dict = df.to_dict(orient='records')
        # Return wrapped in the response model
        return {"books": dict}
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": f"Failed to process CSV file: {str(e)}"}
        ) 