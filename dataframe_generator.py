# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 09:26:57 2016

@author: Zachery McKinnon
"""
import glob
import pandas as pd
import logging

def df_read_and_join(folder_of_csv, index):
    #Takes a folder full of csv's with a common index column and 
    #returns a single dataframe with all the data. 
    #Column names are renamed based on order of file read 
    #(e.g. columns in the first file read will receive suffix of _f1)""" 
    
    
    #reads csv and places them in dictionary
    allFiles = glob.glob(folder_of_csv + "/*.csv")
    df_dict = {}
    key = 1
    for file_ in allFiles:
       df_dict[key] = pd.read_csv(file_, index_col=index, header=0)
       key += 1

    for suffix, input_df in df_dict.items():
        renamer_dict = {}
        for col in list(input_df.columns):
            renamer_dict[col] = col + "_f" + str(suffix)
        input_df.rename(columns=renamer_dict, inplace=True)

        # join columns
    df = None
        if df is None:
            df = input_df
        else:
            df = df.join(input_df, how='outer')
        logging.debug("Shape is currently: {}".format(df.shape))
        
    print df

df_read_and_join(r'C:\Users\Zachery McKinnon\Documents\Zillow_ZipCode\ZipTest', 'RegionName')