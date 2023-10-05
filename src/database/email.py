import datetime

from src.domain.mail import Email

email = [
    Email(
        name='Danilo',
        surname='Jezernik',
        email='dani.jezernik@gmail.com',
        content='Testing',
        datum_vnosa=datetime.datetime.now()
    ).dict(by_alias=True)
]
