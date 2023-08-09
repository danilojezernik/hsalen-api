from dataclasses import dataclass


@dataclass
class GlobalError:
    databs: str
    idModal: str
    path: str
    message: str
    time: str
    stack: str
