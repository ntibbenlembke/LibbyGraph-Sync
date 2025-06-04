from fastapi import APIRouter, UploadFile, File, Body, Depends, status
import pandas as pd
from io import StringIO, BytesIO
from models import BookData, LibraryResponse
from fastapi.responses import JSONResponse
from typing import List
from sqlalchemy.orm import Session
from database import get_db
from db_models import Book

router = APIRouter(prefix="/library", tags=["library"])

@router.get("/upload/")
async def get_library_summary():
    return {"message": "Welcome to the library summary API"}

@router.post("/upload/", 
             response_model=LibraryResponse,
             summary="Upload a CSV file with book data",
             description="Converts uploaded file to JSON format and saves to db.",
             response_description="The parsed book data in JSON format")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """
    Converts uploaded file to JSON format and saves to db.
    
    Needs columns:
    - Title (required)
    - Authors (required)
    - Contributors
    - ISBN/UID
    - Format
    - Read Status
    - Date Added
    - etc.
    
    Returns a JSON object.
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
        
        records = df.to_dict(orient='records')
        
        # Save to db
        db_books = []
        for record in records:
            db_book = Book(
                title=record.get('title'),
                authors=record.get('authors'),
                contributors=record.get('contributors'),
                isbn_uid=record.get('isbn/uid'),
                format=record.get('format'),
                read_status=record.get('read status'),
                date_added=record.get('date added'),
                last_date_read=record.get('last date read'),
                dates_read=record.get('dates read'),
                read_count=record.get('read count'),
                moods=record.get('moods'),
                pace=record.get('pace'),
                character_or_plot_driven=record.get('character- or plot-driven?'),
                strong_character_development=record.get('strong character development?'),
                loveable_characters=record.get('loveable characters?'),
                diverse_characters=record.get('diverse characters?'),
                flawed_characters=record.get('flawed characters?'),
                star_rating=record.get('star rating'),
                review=record.get('review'),
                content_warnings=record.get('content warnings'),
                content_warning_description=record.get('content warning description'),
                tags=record.get('tags'),
                owned=record.get('owned?')
            )
            db.add(db_book)
            db_books.append(db_book)
        
        db.commit()
        
        # Return the books using the json model
        response_books = [BookData.model_validate(record) for record in records]
        return {"books": response_books}
    
    except Exception as e:
        db.rollback()
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": f"Failed to process CSV file: {str(e)}"}
        ) 

@router.get("/books/", response_model=LibraryResponse)
async def get_books(db: Session = Depends(get_db)):
    """Get all books from the database"""
    books = db.query(Book).all()
    book_dicts = [book.to_dict() for book in books]
    
    # convert to BookData objects
    response_books = []
    for book_dict in book_dicts:
        try:
            response_books.append(BookData.model_validate(book_dict))
        except Exception as e:
            print(f"Error converting book: {e}")
    
    return {"books": response_books} 