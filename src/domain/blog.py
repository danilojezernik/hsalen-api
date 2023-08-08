import datetime
from dataclasses import dataclass


@dataclass
class Blog:
    naslov: str
    podnaslov: str
    datum_vnosa: datetime
    vsebina: str
