import random
import pandas as pd
import os
    
def read_table(table_name, random_subset = 1, selected_columns = None, read_from_archive=False):
    source_read = "working_csv_data/"
    if read_from_archive: source_read = "archive/"
    
    if not os.path.exists(source_read + table_name + ".csv"):
        print("File doesn't exist, make sure to use correct name, no .csv at the end")
    else:    
        if random_subset > 1: 
            print("random subset has to be equal or under 1")
            random_subset = 1

        return pd.read_csv(source_read + table_name + ".csv", usecols=selected_columns, skiprows=(lambda x: x !=0 and random.random() > random_subset))