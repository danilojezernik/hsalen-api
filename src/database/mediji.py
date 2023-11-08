import datetime

from src.domain.mediji import Mediji

mediji = [
    Mediji(
        naslov_mediji='Naslov Mediji',
        opis_mediji='Opis Mediji',
        datum_mediji='24.6.2022',
        povezava_slika='Video Mediji',
        povezava_mediji='Povezava Mediji',
        datum_vnosa=datetime.datetime.now()
    ).dict(by_alias=True)
]
