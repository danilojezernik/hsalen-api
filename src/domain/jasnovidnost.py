from pydantic import BaseModel


class Jasnovidnost(BaseModel):
    naslov: str
    podnaslov: str
    jasnovidnost: str
    omogoca: str
