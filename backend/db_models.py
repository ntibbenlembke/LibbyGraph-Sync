from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base
import json
from typing import List, Optional, Dict, Any

class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    authors = Column(String, nullable=False)
    contributors = Column(String, nullable=True)
    isbn_uid = Column(String, nullable=True)
    format = Column(String, nullable=True)
    read_status = Column(String, nullable=True)
    date_added = Column(String, nullable=True)
    last_date_read = Column(String, nullable=True)
    dates_read = Column(String, nullable=True)
    read_count = Column(Integer, nullable=True, default=0)
    moods = Column(String, nullable=True)
    pace = Column(String, nullable=True)
    character_or_plot_driven = Column(String, nullable=True)
    strong_character_development = Column(String, nullable=True)
    loveable_characters = Column(String, nullable=True)
    diverse_characters = Column(String, nullable=True)
    flawed_characters = Column(String, nullable=True)
    star_rating = Column(Float, nullable=True)
    review = Column(Text, nullable=True)
    content_warnings = Column(String, nullable=True)
    content_warning_description = Column(Text, nullable=True)
    tags = Column(String, nullable=True)
    owned = Column(String, nullable=True)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert model to dictionary for API responses"""
        return {
            "id": self.id,
            "title": self.title,
            "authors": self.authors,
            "contributors": self.contributors,
            "isbn/uid": self.isbn_uid,
            "format": self.format,
            "read status": self.read_status,
            "date added": self.date_added,
            "last date read": self.last_date_read,
            "dates read": self.dates_read,
            "read count": self.read_count,
            "moods": self.moods,
            "pace": self.pace,
            "character- or plot-driven?": self.character_or_plot_driven,
            "strong character development?": self.strong_character_development,
            "loveable characters?": self.loveable_characters,
            "diverse characters?": self.diverse_characters,
            "flawed characters?": self.flawed_characters,
            "star rating": self.star_rating,
            "review": self.review,
            "content warnings": self.content_warnings,
            "content warning description": self.content_warning_description,
            "tags": self.tags,
            "owned?": self.owned
        } 