from src.domain.user import User

user = [
    User(
        username='dani',
        email='dani.jezernik@gmail.com',
        full_name='Danilo Jezernik',
        hashed_password='$2b$12$06OF0P6fLEJrCSOoDBmyQuuJyX8Fiefyrm9zMA0tMOPNLwwkRDCyW',
        disabled=False
    ).dict(by_alias=True)
]
