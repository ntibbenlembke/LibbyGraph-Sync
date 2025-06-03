from pydantic import BaseModel, Field
from typing import Optional, List


class BookData(BaseModel):
    title: str
    authors: str
    contributors: Optional[str] = None
    isbn_uid: Optional[str] = Field(None, alias="ISBN/UID")
    format: Optional[str] = None
    read_status: Optional[str] = Field(None, alias="Read Status")
    date_added: Optional[str] = Field(None, alias="Date Added")
    last_date_read: Optional[str] = Field(None, alias="Last Date Read")
    dates_read: Optional[str] = Field(None, alias="Dates Read")
    read_count: Optional[int] = Field(0, alias="Read Count")
    moods: Optional[str] = None
    pace: Optional[str] = None
    character_or_plot_driven: Optional[str] = Field(None, alias="Character- or Plot-Driven?")
    strong_character_development: Optional[str] = Field(None, alias="Strong Character Development?")
    loveable_characters: Optional[str] = Field(None, alias="Loveable Characters?")
    diverse_characters: Optional[str] = Field(None, alias="Diverse Characters?")
    flawed_characters: Optional[str] = Field(None, alias="Flawed Characters?")
    star_rating: Optional[float] = Field(None, alias="Star Rating")
    review: Optional[str] = None
    content_warnings: Optional[str] = Field(None, alias="Content Warnings")
    content_warning_description: Optional[str] = Field(None, alias="Content Warning Description")
    tags: Optional[str] = None
    owned: Optional[str] = Field(None, alias="Owned?")
    
    class Config:
        populate_by_name = True
        

class LibraryResponse(BaseModel):
    books: List[BookData] 