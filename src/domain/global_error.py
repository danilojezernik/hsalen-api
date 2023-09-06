from typing import Optional

from pydantic import BaseModel, Field


class GlobalError(BaseModel):
    id: Optional[str] = Field(alias='_id')
    databs: str
    idModal: str
    path: str
    message: str
    time: str
    stack: str
