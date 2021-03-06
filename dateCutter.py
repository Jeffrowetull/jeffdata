import pandas as pd
'''
A little function that will split the date into three
separate columns and make a new dataframe
'''


def splitter(series):
    dates = []
    for i in series:
        cut = i.split('/')
        dates.append(cut)
    df = pd.DataFrame(dates, columns=['Month', 'Day', 'Year'])
    return df