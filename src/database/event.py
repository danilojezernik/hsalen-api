import datetime

from src.domain.events import Events

event = [
    Events(
        event='Hipnoza in hipnoterapija',
        content='Lsto.',
        location='Mozirje',
        start_date='24.06.2024',
        start_time='14:30',
        event_length='5h',
        show_notification=False,
        datum_vnosa=datetime.datetime.now()
    ).dict(by_alias=True)
]
