from dataclasses import asdict

from src.domain.knjiga import Knjiga

knjiga = [
    asdict(
        Knjiga(
            naslov='Knjiga naslov',
            podnaslov='Knjiga Podnaslov',
            opis='Knjiga opis'
        )
    )
]
