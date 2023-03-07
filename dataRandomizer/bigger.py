import pandas as pd
    
def data_multiply(dataframe, multiplier):
    """   
    Make your random sample exponetially bigger!
    """
    n = 0
    while n < multiplier:
        bigger_dataframe = pd.concat([dataframe, dataframe])
        n = n+1