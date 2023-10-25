import datetime

from src.domain.newsletter import Newsletter

newsletter = [
    Newsletter(
        name='Danilo',
        surname='Jezernik',
        email='samhara.sadhaka@gmail.com',
        datum_vnosa=datetime.datetime.now()
    ).dict(by_alias=True),
    Newsletter(
        name='Dani',
        surname='Jez',
        email='danilo.jezernik@gmail.com',
        datum_vnosa=datetime.datetime.now()
    ).dict(by_alias=True),
    Newsletter(
        name='Alen',
        surname='M',
        email='alen.maric75@gmail.com',
        datum_vnosa=datetime.datetime.now()
    ).dict(by_alias=True)
]
