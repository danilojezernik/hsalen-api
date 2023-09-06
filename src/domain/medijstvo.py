from dataclasses import dataclass

from pydantic import BaseModel


class Medijstvo(BaseModel):
    naslov: str
    podnaslov: str
    medijstvo: str
    tavanje_dus: str
