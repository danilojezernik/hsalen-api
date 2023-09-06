from typing import Optional

from pydantic import BaseModel, Field


class Hipnoterapija(BaseModel):
    id: Optional[str] = Field(alias='_id')
    naslov: str
    podnaslov: str
    hipnoza: str
    hipnoterapija: str
