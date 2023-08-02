from dataclasses import asdict

from src.domain.hipnoterapija import Hipnoterapija

hipnoterapija = [
    asdict(
        Hipnoterapija(
            naslov='Hipnoterapija naslov',
            podnaslov='Hipnoterapija Podnaslov',
            hipnoza='Kaj je Hipnoterapija?',
            hipnoterapija='Kaj je hipnoterapija?'
        )
    )
]
