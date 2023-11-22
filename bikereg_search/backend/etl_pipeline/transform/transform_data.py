import pandas as pd
import numpy as np

from extract import get_events
import scripts

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


#Event Address transformation
event_df.EventAddress = convert_empty_string_to_numpy_nan(events_df.EventAddress)

#Event City transformation
event_df.EventCity = convert_empty_string_to_numpy_nan(events_df.EventCity)