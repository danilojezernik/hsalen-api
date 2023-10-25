import datetime

from src import env
from src.domain.newsletter import Newsletter

newsletter = [
    Newsletter(
        name='Danilo',
        surname='Jezernik',
        email=env.EMAIL_1,
        datum_vnosa=datetime.datetime.now()
    ).dict(by_alias=True),
    Newsletter(
        name='Dani',
        surname='Jez',
        email=env.EMAIL_2,
        datum_vnosa=datetime.datetime.now()
    ).dict(by_alias=True),
    Newsletter(
        name='Alen',
        surname='M',
        email=env.EMAIL_3,
        datum_vnosa=datetime.datetime.now()
    ).dict(by_alias=True)
]
