import datetime
from dataclasses import dataclass


@dataclass
class Blog:
    naslov: str
    tag: str
    podnaslov: str
    datum_vnosa: datetime
    vsebina: str
