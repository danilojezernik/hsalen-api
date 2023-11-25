from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class Review(BaseModel):
    id: Optional[str] = Field(alias='_id', default_factory=lambda: str(ObjectId()))
    name: str
    content: str
