from dataclasses import dataclass

from pydantic import BaseModel


class Mediji(BaseModel):
    naslov_mediji: str
    opis_mediji: str
    video_mediji: str
    povezava_mediji: str