from dataclasses import asdict

from src.domain.samohipnoza import Samohipnoza

samohipnoza = [
    asdict(
        Samohipnoza(
            naslov='Samohipnoza naslov',
            podnaslov='Samohipnoza Podnaslov',
            samohipnoza='Kaj je samohipnoza?',
            pomaga='Kje lahko pomaga?'
        )
    )
]
