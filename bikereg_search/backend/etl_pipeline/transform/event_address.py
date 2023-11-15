def convert_emtpy_string(event_str: str) -> str:
    """
    Function to convert an empty string to a "NULL" string. "NULL" strings will be converted to a numpy NaN so it can be a sql "NULL" when writen to a database.
    The numpy conversion is done in bulk in a later step.

    Arguments:
    string: string from events API to be checked if it is empty
    """

    if len(event_str) == 1:
        event_str = "NULL"


if __name__ == "__main__":
    convert_emtpy_string
