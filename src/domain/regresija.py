from dataclasses import dataclass

from pydantic import BaseModel


class Regresija(BaseModel):
    naslov: str
    podnaslov: str
    regresija: str
    preteklost: str