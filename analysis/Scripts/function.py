import pandas as pd
import numpy as np
import seaborn as sns

#Wrapping method chains in a function:
def load_process(url_or_path_to_csv_file):
    
    
    # Method Chain 1 (Load data and deal with missing data)
    data = (pd.read_csv(url_or_path_to_csv_file) 
            .dropna()
            .drop(columns =['Unnamed: 0',' 0'])
            .drop([' 77516',' Never-married',' 2174',' 13'], axis =1 )
        
        )
    # Method Chain 2 (Create new columns, drop others, and do processing)
    data2 = (
        data
        .rename(columns= {'39': 'Age'})
        .rename(columns= {' Bachelors': 'Education'})
        .rename(columns={' State-gov': 'Work Class'})
        .rename(columns= {' Adm-clerical': 'Occupation'})
        .rename(columns= {' Not-in-family': 'Relationship'})
        .rename(columns= {' White': 'Race'})
        .rename(columns= {' Male': 'Sex'})
        .rename(columns= {' 40': 'Hours/Week'})
        .rename(columns= {' United-States': 'Native Country'})
        .rename(columns= {' <=50K': 'Salary'})
    )
    
    #data_to_csv(r"C:\Users\Amrita\Desktop\Data301\course-project-group_1029\data\raw\adult.csv")
    return data2

    
    
  