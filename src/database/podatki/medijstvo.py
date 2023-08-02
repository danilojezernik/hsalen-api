from dataclasses import asdict

from src.domain.medijstvo import Medijstvo

medijstvo = [
    asdict(
        Medijstvo(
            naslov='Medijstvo naslov',
            podnaslov='Medijstvo Podnaslov',
            medijstvo='Kaj je medijstvo?',
            tavanje_dus='Vzroki tavanja duš?'
        )
    )
]
