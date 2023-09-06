from dataclasses import dataclass

from pydantic import BaseModel


class Index(BaseModel):
    naslov: str
    podnaslov: str
    pomoc_hipnoterapija: str
    pomoc_jasnovidnsot: str
    pomoc_medijstvo: str
