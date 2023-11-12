import datetime
import re


def parse_timestamp(timestamp: str):
    """
    Dates are initial in the form of "/Date(1698379200000-0400)/".
    This functions parses the string to extract the date and time zone.

    Arguments:
    Epoch time stamp in the form of "/Date(1698379200000-0400)/"

    Returns:
        List of:
            Millisecond epoch time stamp as string
            Time zone difference from GMT

    Example:
    "/Date(1698379200000-0400)/" --> ["1698379200000", "0400"]
    """

    return re.split(r"[()]", timestamp)[1].split("-")


def to_date(timestamp: str):
    """
    Converts
    """

    return datetime.datetime.fromtimestamp(int(timestamp) / 1000)


def convert_time_stamp(event_start_timestamp: str, event_end_timestamp: str):
    timestamps = [event_start_timestamp, event_end_timestamp]

    start, end = list(map(parse_timestamp, timestamps))

    start_timestamp, start_time_zone = start
    end_timestamp, end_time_zone = end

    start_date, end_date = list(map(to_date, [start_timestamp, end_timestamp]))

    return start_date, start_time_zone, end_date, end_time_zone


if __name__ == "__main__":
    convert_time_stamp()
