from dataclasses import asdict

from src.domain.jaz import Jaz

jaz = [
    asdict(
        Jaz(
            ime_priimek='Alen',
            o_meni='O meni',
            naslov_mediji='Naslov Mediji',
            opis_mediji='Opis Mediji',
            video_mediji='Video Mediji',
            povezava_mediji='Povezava Mediji'
        )
    )
]
