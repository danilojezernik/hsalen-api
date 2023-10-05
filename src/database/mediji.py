from src.domain.mediji import Mediji

mediji = [
    Mediji(
        naslov_mediji='Naslov Mediji',
        opis_mediji='Opis Mediji',
        povezava_slika='Video Mediji',
        povezava_mediji='Povezava Mediji'
    ).dict(by_alias=True)
]
