from dataclasses import asdict

from src.domain.global_error import GlobalError

global_error = [
    asdict(
        GlobalError(
            databs='#modalexample',
            id='modalExample',
            path='Naslov Mediji',
            message='Opis Mediji',
            handler='Video Mediji',
            time='Povezava Mediji',
            stack='error'
        )
    )
]