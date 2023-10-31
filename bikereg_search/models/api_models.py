from pydantic import BaseModel, HttpUrl

class Event(BaseModel):
    EventCategories
    Distance: PositiveFloat
    EventAddress: str
    EventCity: str
    EventDate
    EventEndDate
    EventId
    EventName
    EventNotes
    EventState
    EventTypes
    Eventurl: HttpUrl
    EventWebsite: HttpUrl
    EventZip
    EventLatitude
    EventLongitude
    EventRegCloseDate    
    EventRegOpenDate