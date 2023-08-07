from dataclasses import asdict

from src.domain.mediji import Mediji

mediji = [
    asdict(
        Mediji(
            naslov_mediji='Naslov Mediji',
            opis_mediji='Opis Mediji',
            video_mediji='Video Mediji',
            povezava_mediji='Povezava Mediji'
        )
    )
]
