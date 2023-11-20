from src.domain.user import User

user = [
    User(
        username='alenmaric',
        email='dani.jezernik@gmail.com',
        full_name='Danilo Jezernik',
        hashed_password='$2b$12$3USFBYwoE3Bp9xTGO/ugxurb8S3ZUhWdXe1f4SKHLLpMGyzrKLVVu',
        disabled=False
    ).dict(by_alias=True)
]
