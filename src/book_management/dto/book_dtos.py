from typing import List, Optional
from datetime import date

from pydantic import BaseModel, Field


class BookDTO(BaseModel):
    id: Optional[int]
    title: str
    author_id: int
    publication_date: date = Field(default_factory=date.today)

    class Config:
        orm_mode = True


class BookListDTO(BaseModel):
    __root__: List[BookDTO]

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True
