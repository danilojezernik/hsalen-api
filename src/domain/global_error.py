from dataclasses import dataclass


@dataclass
class GlobalError:
    path: str
    message: str
    handler: str
    time: str
    stack: str
