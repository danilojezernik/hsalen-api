from pydantic import BaseModel


class Samohipnoza(BaseModel):
    naslov: str
    podnaslov: str
    samohipnoza: str
    pomaga: str
