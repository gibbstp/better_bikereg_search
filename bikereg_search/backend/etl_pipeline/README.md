# Description  

ETL pipeline for extracting BikeReg Event data from BikeReg Event Search API.  

[BikeReg documentation](https://www.bikereg.com/api/EventSearchDoc.aspx)  

## ETL Pipeline  
File serves as an "orchestration" process. Contains settings and is responsible for calling individual ETL files. 

### Extraction:
`extract > get_events.py`
Data is extracted from BikeReg API in a `while` loop. Code breaks out of `while` loop when the number of results from the API call is less than 100. This value is returned by BikeReg API as `ResultsCount`.  

The API will always return a status of 200 regardless of whether the call returned any data or not. This has been tested by passing in non-sensical and non-documented parameters. All return a status of 200. 

### Transform  
`transform > transform_data.py`
Data 