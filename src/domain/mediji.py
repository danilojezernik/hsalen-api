from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class Mediji(BaseModel):
    id: Optional[str] = Field(alias='_id', default_factory=lambda: str(ObjectId()))
    naslov_mediji: str
    opis_mediji: str
    povezava_slika: str
    povezava_mediji: str
