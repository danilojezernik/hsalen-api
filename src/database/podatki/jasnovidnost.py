from dataclasses import asdict

from src.domain.jasnovidnost import Jasnovidnost

jasnovidnost = [
    asdict(
        Jasnovidnost(
            naslov='Jasnovidnost naslov',
            podnaslov='Jasnovidnost Podnaslov',
            jasnovidnost='Kaj je jasnovidnost?',
            omogoca='Kaj nam omogoča?'
        )
    )
]
