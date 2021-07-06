#!/opt/anaconda3/bin/python
# -*- coding: utf-8 -*-

import os
import time
import glob
from dfply import *

import pandas as pd

from price_detection_tools import screener, add_label


if __name__ == '__main__':

    # Path to dataset directory
    # TODO:
    path = "/Users/d.e.magno/Datasets/stocks_with_industry"

    # Path to destination directory
    dest_folder = "/Users/d.e.magno/Projects/Price Pattern"

    # TODO:
    f_file = os.path.join(dest_folder, 'new_patterns.csv')

    # Store all filenames as a list
    all_files = glob.glob(os.path.join(path, '*.csv'))

    # Initialize dataframe for storage 
    all_patterns = pd.DataFrame()

    # Loop over all csv files in the dataset directory
    for i, filename in enumerate(all_files):

        # Progress report
        print(f"{i+1}: Extracting pattern from {filename}...")

        # Import data
        df = pd.read_csv(filename)

        # Detect patterns and store as dataframe
        # Merge all patterns in a single dataframe
        try:
            patterns = (df >>
                        screener >>
                        add_label(df))
            patterns['industry'] = df.Industry[0]
            all_patterns = pd.concat(
                [all_patterns, patterns]).reset_index(drop=True)
            all_patterns.to_csv(f_file)
            print("Done.")
            print()
        except KeyboardInterrupt:
            break
        except Exception:
            print("Skipped.")
            print()
            pass
        
    # TODO:
    #all_patterns.to_csv(f_file)
    print()
    print("Finished.")
    

