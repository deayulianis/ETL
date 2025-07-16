def save_to_csv(dataframe, filename):
    dataframe.to_csv(filename, index=False)