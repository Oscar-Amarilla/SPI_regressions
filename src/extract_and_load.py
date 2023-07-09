import pandas as pd
import numpy as np
import os
from .config import INPUT_DIR

def extract_and_load(input_dir=INPUT_DIR):

    # Listing all the files in the input directory
    files_list = os.listdir(input_dir)

    #Initilazing the database dictionary. 
    database = {}
    # The elements in the dictionary will have the following estructre:
    # {key:location of the station, value: SPI values dataframe}
    # In the case of the MEI.csv
    # {key:mei, value: MEI values dataframe}
    
    # Extracting the data and placing it into the dataset 
    for file in files_list:
        if file != 'MEI.csv':
            table_name = file.split('_')[0].lower()
            database[table_name]= pd.read_csv(f"{input_dir}/{file}",delimiter=',')
        else:
            table_name = file.split('.')[0].lower()
            database[table_name]= pd.read_csv(f"{input_dir}/{file}",delimiter=',')

    return database
