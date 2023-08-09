from dataclasses import dataclass


@dataclass
class GlobalError:
    databs: str
    id: str
    path: str
    message: str
    handler: str
    time: str
    stack: str
