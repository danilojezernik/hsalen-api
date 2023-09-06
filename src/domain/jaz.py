from dataclasses import dataclass

from pydantic import BaseModel


class Jaz(BaseModel):
    ime_priimek: str
    o_meni: str