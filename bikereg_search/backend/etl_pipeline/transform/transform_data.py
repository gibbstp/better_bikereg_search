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
    "EventTypes": "str",
    "EventWebsite": "str",
    "EventZip": "str",
    "Latitude": "float64",
    "Longitude": "float64",
    "RegCloseDate": "str",
    "RegOpenDate": "str",
}

event_df = pd.DataFrame(bikereg_event, dtype=dtypes)


# Event Address transformation
event_df.EventAddress = scripts.convert_empty_string_to_numpy_nan(event_df.EventAddress)

# Event City transformation
event_df.EventCity = scripts.convert_empty_string_to_numpy_nan(event_df.EventCity)

# Event Date transformation
