import pandas as pd
import numpy as np
import seaborn as sns

#Wrapping method chains in a function:
def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
            pd.read_csv(url_or_path_to_csv_file)
            .dropna()
            .drop(columns =['Unnamed: 0',' 0'])
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
        df1
        .rename(columns= {'39': 'Age'})
        .rename(columns= {' 77516': 'fnlwgt'})
        .rename(columns= {'education': 'Education'})
        .rename(columns= {' 13': 'Education-Num'})
        .rename(columns= {' Never-married': 'Marital-Status'})
        .rename(columns= {' Adm-clerical': 'Occupation'})
        .rename(columns= {' Not-in-family': 'Relationship'})
        .rename(columns= {' White': 'Race'})
        .rename(columns= {' Male': 'Sex'})
        .rename(columns= {' 2174': 'Capital-Gain'})
        .rename(columns= {' 40': 'Hours/Week'})
        .rename(columns= {' United-States': 'Native Country'})
      )

    # Make sure to return the latest dataframe

    return df2 
    load_and_process(r"C:\Users\Amrita\Desktop\Data301\course-project-group_1029\data\raw\adult.data")