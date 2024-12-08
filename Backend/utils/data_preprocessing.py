import pandas as pd

def preprocess_data(data):
    # Example of preprocessing logic
    df = pd.DataFrame(data)
    df.fillna(0, inplace=True)  # Replace missing values with 0
    return df
