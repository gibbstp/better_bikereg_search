from pydantic import BaseModel, HttpUrl, PositiveFloat
from decimal import Decimal

class Event(BaseModel):
    EventCategories: 
    Distance: PositiveFloat
    EventAddress: str
    EventCity: str
    TimeZone: int
    EventDate: int
    EventEndDate: int
    EventId: int
    EventName: str
    EventNotes: str
    EventState: str
    EventTypes: list
    Eventurl: HttpUrl
    EventWebsite: HttpUrl
    EventZip: int
    EventLatitude: Decimal
    EventLongitude: Decimal
    EventRegCloseDate: int
    EventRegOpenDate: int