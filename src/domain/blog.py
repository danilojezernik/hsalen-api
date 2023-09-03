import datetime

from pydantic import BaseModel


class Blog(BaseModel):
    naslov: str
    tag: str
    podnaslov: str
    datum_vnosa: datetime.datetime
    vsebina: str
