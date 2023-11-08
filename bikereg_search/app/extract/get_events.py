import requests
import time
import pandas as pd


def api_url_generator(page_number: int) -> str:
    """
    Generator for bikereg api urls

    Arguments:
    api page number: int

    Returns:
    url with page number: str
    """
    return f"https://www.bikereg.com/api/search?page={page_number}"


def request_api(url: str):
    """
    Generator to request api

    Arguments:
    api_url_generator url: str

    Returns:
    Bike reg api response: json
    """
    return requests.get(url).json()


def process_url_response(events_df: pd.DataFrame, url_response) -> pd.DataFrame:
    """ "
    Function to convert api response into pandas dataframe then concatenate response
    to storage dataframe.

    Arguments:
    storage dataframe: pandas dataframe
    Bike reg api response: json

    Returns:
    Storage dataframe with new reponse: pandas dataframe
    """
    # response["MatchingEvents"] is a list of dictionaries
    response_events_df = pd.DataFrame(url_response["MatchingEvents"])

    return pd.concat([events_df, response_events_df], axis=0, ignore_index=True)


def bike_reg_api(page_number: int, events_df: pd.DataFrame) -> int:
    """
    Function to wrap necesary steps to api

    Argunments:
    API page number: int
    Storage dataframe: pandas dataframe

    Returns:
    tuple: (storage_dataframe, reponse results count)
    """
    url = api_url_generator(page_number=page_number)

    response = request_api(url=url)

    events_df = process_url_response(events_df=events_df, url_response=response)

    return events_df, response["ResultCount"]


page_number = 0
events_df = pd.DataFrame()

events_df, results_count = bike_reg_api(page_number=page_number, events_df=events_df)

while results_count == 100:
    results_count = bike_reg_api(page_number=page_number, events_df=events_df)

    page_number += 1

    # Bikreg api does not have a robots.txt or a known rate limit
    # sleep is added here to be nice.
    time.sleep(0.5)
