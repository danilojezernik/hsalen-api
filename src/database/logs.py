import datetime

from src.domain.logs import Logging

backend_logs = [
    Logging(
        route_action='route_action',
        domain='PRIVATE',
        content='content',
        client_host='localhost',
        city='Mozirje',
        datum_vnosa=datetime.datetime.now()
    ).dict(by_alias=True)
]
