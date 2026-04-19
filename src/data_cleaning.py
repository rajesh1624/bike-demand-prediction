import pandas as pd
def load_data(path):
    # read the dataset
    df = pd.read_csv(path)
    return df
def clean_data(df):
    # drop the columns that are not needed for analysis
    df = df.drop(columns=['instant', 'dteday', 'casual', 'registered'],axis=1)
    return df  
   

   