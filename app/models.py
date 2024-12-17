from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Blog(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    content: str = Field(..., min_length=10)
    author: str = Field(..., min_length=3, max_length=50)
    published_at: Optional[datetime] = None
    tags: Optional[list[str]] = []

    class Config:
        schema_extra = {
            "example": {
                "title": "Introduction to FastAPI",
                "content": "FastAPI is a modern web framework for Python...",
                "author": "John Doe",
                "published_at": "2024-12-01T10:00:00",
                "tags": ["FastAPI", "Python", "Web Development"]
            }
        }
