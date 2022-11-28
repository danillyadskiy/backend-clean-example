from typing import Optional

from pydantic import BaseModel


class Author(BaseModel):
    id: int
    login: str
    first_name: Optional[str]
    last_name: Optional[str]
