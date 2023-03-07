import pandas as pd
import random

def read_file(file, type):
    """
    Read input file
    """
    if type == 'csv':
        dataframe = pd.read_csv(file)
    elif type == 'excel':
        dataframe = pd.read_excel(file)
    return dataframe

def data_scramble(dataframe):
    """
    Input is a DataFrame and output is the same DataFrame 
    with the values in the columns scrambled into different places.
    """
    randomized_sample = pd.DataFrame()
    cols = dataframe.columns

    for item in cols:
        print(item)
        n = 0
        list = []
        while n <= 1000:
            random_index = random.randint(0, len(dataframe))
            list.append(dataframe.iloc[random_index][item])
            n = n+1
        randomized_sample[item] = list
    
    return randomized_sample

def new_file(old_file_name, dataframe, type):
    if type == 'csv':
        new_filename = old_file_name.rstrip('.csv') + '_randomized.csv'
        dataframe.to_csv(new_filename)
    elif type =='excel':
        new_filename = old_file_name.rstrip('.xlsx') + '_randomized.xlsx'
        dataframe.to_excel(new_filename)
    print(f'{new_filename} file created in the current working directory.')