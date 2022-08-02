from typing import List, Optional
from pydantic import BaseModel


class AuthorDTO(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    email: str

    class Config:
        orm_mode = True


class AuthorListDTO(BaseModel):
    __root__: List[AuthorDTO]

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True
