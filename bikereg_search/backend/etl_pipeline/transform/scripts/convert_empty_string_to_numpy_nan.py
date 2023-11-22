def convert_empty_string_to_numpy_nan(pd_series: pd.Series) -> pd.Series:
    """
    Function to convert an empty string to a numpy NaN so it can be a sql "NULL" when writen to a database.

    Arguments:
    Pandas Series: pandas series from event dataframe
    """

    series_mask = pd_series.str.isspace()
    pd_series[series_mask] = np.NaN
    
    return pd_series


if __name__ == "__main__":
    convert_empty_string_to_numpy_nan()
