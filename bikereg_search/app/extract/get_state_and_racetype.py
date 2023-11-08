from bs4 import BeautifulSoup as bs
import requests
import json


def get_dropdown_options(bs4_soup):
    """function to scrape the region and race types found in Bikereg Event calendar dropdown menues.
    The scraped values are used in the UI to provide options for searching event.
    All available options from bikereg are collected and processed.
    Writes processed html to json file.

    Arguments:
    BeautifulSoup4 parsed html response.

    Returns:
    None
    """

    url = "https://www.bikereg.com/Events/"

    response = requests.get(url)

    soup = bs(response.text, "html.parser")

    # html names of dropdown menus Event Type and Event Location, respectively
    dropdown_menu_html_names = [
        "ctl00$ContentPlaceHolder1$cboType",
        "ctl00$ContentPlaceHolder1$cboRegion",
    ]

    race_type, race_location = {}, {}

    dropdown_menu_names_dict = [race_type, race_location]

    for dropdown_menu_html_name, dropdown_menu_name in zip(
        dropdown_menu_html_names, dropdown_menu_names_dict
    ):
        # first element in options is the selected option in dropdown; therefore, skipping to get options
        dropdown_menu_options = bs4_soup.find(
            attrs={"name": dropdown_menu_html_name}
        ).find_all("option")[1:]

        for dropdown_menu_option in dropdown_menu_options:
            # selecting state name of race type name
            option_text = dropdown_menu_option.text

            # selecting state abbreviation or race integer reference
            option_value = dropdown_menu_option["value"]

            dropdown_menu_name[option_text] = option_value

    write_to_json(race_type, race_location)


def write_to_json(scraped_race_types: dict, scraped_race_locations: dict):
    with open(f"/app/bikereg_search/data/race_type.json", "w") as f:
        json.dump(scraped_race_types, f)

    with open(f"/app/bikereg_search/data/race_locations.json", "w") as f:
        json.dump(scraped_race_locations, f)


if __name__ == "__main__":
    get_dropdown_options()
