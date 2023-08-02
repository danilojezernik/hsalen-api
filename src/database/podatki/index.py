from dataclasses import asdict

from src.domain.index import Index

index = [
    asdict(
        Index(
            naslov='Index naslov',
            podnaslov='Index Podnaslov',
        )
    )
]
