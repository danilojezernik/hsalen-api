import datetime

from src.domain.events import Events

event = [
    Events(
        event='Hipnoza in hipnoterapija',
        content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam sollicitudin eu eros nec tempus. Nunc nec dignissim odio, '
                'eu sodales urna. Maecenas fringilla, nibh vel consectetur tincidunt, felis tortor accumsan nisi, vitae ultrices leo augue '
                'dictum metus. Mauris vel fermentum elit. Curabitur sed arcu eget risus varius eleifend non ac dui. Ut porttitor pretium sem '
                'nec commodo. Morbi ex massa, volutpat sed imperdiet a, convallis non tellus. Etiam auctor justo odio, in porttitor ex '
                'placerat nec. Pellentesque sed fringilla dolor. Ut quis volutpat arcu, id finibus nunc. Aliquam sed metus vitae nunc '
                'porttitor gravida quis sit amet lectus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia '
                'curae; Vivamus tincidunt gravida massa, ut tincidunt erat hendrerit nec. Nam id nulla justo.',
        location='Mozirje',
        start_date='24.06.2024',
        event_length='5h',
        show_notification=True,
        datum_vnosa=datetime.datetime.now()
    ).dict(by_alias=True)
]
