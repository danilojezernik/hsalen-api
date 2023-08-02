from dataclasses import asdict

from src.domain.blog import Blog

blog = [
    asdict(
        Blog(
            naslov='Blog Naslov Test podatki',
            podnaslov='Blog Podnaslov',
            vsebina='Vsebina Blog'
        )
    )
]
