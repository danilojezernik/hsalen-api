from src.domain.user import User

user_seed = [
    User(
        username='dani',
        email='dani.jezernik@gmail.com',
        full_name='Danilo Jezernik',
    ).dict(by_alias=True)
]
