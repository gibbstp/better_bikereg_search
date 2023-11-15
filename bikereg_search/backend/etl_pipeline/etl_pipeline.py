import pandas as pd

from extract import get_events

# returns list of dicts
bikereg_event = get_events()

dtypes = {
    "Categories": "object",
    "EventAddress": "str",
    "EventCity": "str",
    "EventDate": "str",
    "EventEndDate": "str",
    "EventId": "int",
    "EventName": "str",
    "EventPermalink": "str",
    "EventType": "str",
    "EventWebsite": "str",
    "EventZip": "str",
    "Latitude": "float64",
    "Longitude": "float64",
    "RegCloseDate": "str",
    "RegOpenDate": "str",
}

event_df = pd.Dataframe(bikereg_event, dtypes=dtypes)
