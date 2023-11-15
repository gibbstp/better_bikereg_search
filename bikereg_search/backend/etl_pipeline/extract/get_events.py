import requests, time


def api_url_generator(page_number: int) -> str:
    """
    Generate BikeReg API URLs based on the page number.

    Arguments:
    page_number (int): The page number for the API request.

    Returns:
    str: The generated API URL.
    """
    return f"https://www.bikereg.com/api/search?page={page_number}"


def request_api(url: str):
    """
    Request data from the BikeReg API.

    Arguments:
    url (str): The URL for the API request.

    Returns:
    json: BikeReg API response in JSON format.
    """
    
    #TODO: add logging for requests reponse.
    #TODO: add individual request exceptions. RequestException is too general and doesn't provide enough granulatiry
    try:
        response = requests.get(url).json()
    
    except requests.exceptions.RequestException as e:
        SystemExit
        
    
def api_error(api_response: requests.Response):
    """
    API call error handling
    
    #TODO: add more granularity to errors handling"""
    
    
    


'''
#TODO: remove this function. Rewrote code to make this repetitive. Leaving until certain. 
def process_url_response(events_list: list, url_response) -> list:
    """
    Process BikeReg API response and extend existing list.

    Arguments:
    events_list (list): The existing list to which the API response will be added.
    url_response: BikeReg API response in JSON format.

    Returns:
    list: The updated list with the new API response events.
    """
    
    # response["MatchingEvents"] is a list of dictionaries
    return events_list.extend(url_response["MatchingEvents"])
    '''


def bike_reg_api(page_number: int = 0) -> tuple(list[dict], int):
    """
    Perform necessary steps to fetch data from the BikeReg API.

    Argunments:
    page_number (int): The API page number.
    events_list (pd.DataFrame): The existing DataFrame to which the API response will be added.

    Returns:
    int: result_count: int
    """

    url = api_url_generator(page_number=page_number)

    response = request_api(url=url)

    # TODO: add logging for number of events in response for each page number
    results_count = response["ResultCount"]

    return response["MatchingEvents"], results_count


def main() -> list[dict]:
    """
    Perform an iterative loop to fetch data from the BikeReg API until the result count all results are collected.

    Returns:
    list: The final list containing all the fetched data.
    """
    page_number = 0
    events_list = []

    events_list, results_count = bike_reg_api()

    while results_count == 100:
        response_events, results_count = bike_reg_api(page_number=page_number)

        # TODO: add logging for length of list after extend
        events_list.extend(response_events)

        page_number += 1

        # Bikreg api does not have a robots.txt or a known rate limit
        # sleep is added here to be nice.
        time.sleep(0.5)

    return events_list


if __name__ == "__main__":
    main()
