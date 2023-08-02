from dataclasses import asdict

from src.domain.regresija import Regresija

regresija = [
    asdict(
        Regresija(
            naslov='Regresija naslov',
            podnaslov='Regresija Podnaslov',
            regresija='Kaj je regresija?',
            preteklost='Pretekla življenja?'
        )
    )
]
