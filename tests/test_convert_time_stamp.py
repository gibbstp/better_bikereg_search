import datetime

from bikereg_search.backend.etl_pipeline.transform.scripts.convert_time_stamp import (
    parse_timestamp,
    to_date,
    convert_time_stamp,
)

def test_parse_timestamp():
    timestamp_string = "/Date(1698379200000-0400)/"

    expected_results = ["1698379200000", "0400"]

    assert parse_timestamp(timestamp_string) == expected_results


def test_to_date():
    expected_results = datetime.datetime(2023, 10, 27, 4, 0)

    assert to_date("1698379200000") == expected_results


def test_convert_time_stamp():
    start_date = "/Date(1698379200000-0400)/"

    end_date = "/Date(1698824800000-0500)"

    expected_results = (
        datetime.datetime(2023, 10, 27, 4, 0),
        "0400",
        datetime.datetime(2023, 11, 1, 7, 46, 40),
        "0500",
    )

    assert convert_time_stamp(start_date, end_date) == expected_results
