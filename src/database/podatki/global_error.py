from src.domain.global_error import GlobalError

global_error = [
    GlobalError(
        databs='#modalexample',
        idModal='modalExample',
        path='Naslov Mediji',
        message='Opis Mediji',
        time='Povezava Mediji',
        stack='error'

    ).dict(by_alias=True)
]
