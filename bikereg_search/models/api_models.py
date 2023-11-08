from pydantic import BaseModel, HttpUrl, PositiveFloat
from decimal import Decimal
from datetime import datetime


class Event(BaseModel):
    EventCategories: tuple
    Distance: PositiveFloat
    EventAddress: str
    EventCity: str
    TimeZone: int
    EventDate: datetime
    EventEndDate: datetime
    EventId: int
    EventName: str
    EventState: str
    EventTypes: tuple
    Eventurl: HttpUrl
    EventWebsite: HttpUrl
    EventZip: int
    EventLatitude: Decimal
    EventLongitude: Decimal
    EventRegCloseDate: datetime
    EventRegOpenDate: datetime
