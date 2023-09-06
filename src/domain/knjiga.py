from dataclasses import dataclass

from pydantic import BaseModel


class Knjiga(BaseModel):
    naslov: str
    podnaslov: str
    opis: str
