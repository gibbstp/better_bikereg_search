from bs4 import BeautifulSoup as bs
import requests

url = "https://www.bikereg.com/Events/"

response = requests.get(url)

soup = bs(response.text, 'html.parser')

def get_dropdown_options(bs4_soup):
    
    #html names of dropdown menus Event Type and Event Location, respectively
    dropdown_menu_html_names = ["ctl00$ContentPlaceHolder1$cboType",
                                "ctl00$ContentPlaceHolder1$cboRegion"]
    
    race_type, race_location = {}, {}
    
    dropdown_menu_names_dict = [race_type,
                                race_location]
    
    for dropdown_menu_html_name, dropdown_menu_name in zip(dropdown_menu_html_names, dropdown_menu_names_dict):
        
        #first element in options is the selected option in dropdown; therefore, skipping to get options
        dropdown_menu_options = bs4_soup.find(attrs={"name": dropdown_menu_html_name}).find_all("option")[1:]
        
        for dropdown_menu_option in dropdown_menu_options:
            
            option_text = dropdown_menu_option.text
            option_value = dropdown_menu_option["value"]
            
            dropdown_menu_name[option_text] = option_value
            
    dropdown_menus = (race_type,race_location)
    
    return dropdown_menus

testing = get_dropdown_options(soup)
print(testing)