import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class Events(BaseModel):
    id: Optional[str] = Field(alias='_id', default_factory=lambda: str(ObjectId()))
    event: str
    content: str
    location: str
    show_notification: bool
    start_date: str
    event_length: str
    datum_vnosa: datetime.datetime = Field(default_factory=datetime.datetime.now)
