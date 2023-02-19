# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 12:27:39 2023

@author: Eric
"""

import pandas as pd


def clean(input1, input2):
    
    # import data    
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)
    
    # rename the column name of df1 so that match with df2 
    df1 = df1.rename(columns={'respondent_id':'id'})
    
    # merge dataframes with common column, namely 'id'
    df3 = pd.merge(df1, df2, on='id')
    
    # change the birthdate coulmn to datetime format 
    df3['birthdate'] = pd.to_datetime(df3['birthdate'], dayfirst=True)
    
    # remove the empty rows
    df3.dropna(inplace=True)
    
    # drop rows in the 'job' column containing 'insurance' or 'Insurance'
    df3 = df3[df3['job'].str.contains("insurance|Insurance") == False]
    
    #shape_of_output_df = str("The shape of output file: ") + str(df3.shape)
    #print(shape_of_output_df)
    
    return df3


if __name__ == '__main__':
    import argparse
    

    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help='Contact info file (CSV)')
    parser.add_argument('input2', help='Other info file (CSV)')
    parser.add_argument('output', help='Output file (CSV)')
    args = parser.parse_args()

    cleaned = clean(args.input1, args.input2)
    cleaned.to_csv(args.output, index=False)
    
print('The shape of the output file:' + str(cleaned.shape))
      
    
    