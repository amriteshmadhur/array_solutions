# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 15:48:37 2023

@author: 0002J0744
"""

import os

def merge_files(output_file, *input_files):
    with open(output_file, 'w') as outfile:
        for input_file in input_files:
            with open(input_file, 'r') as infile:
                outfile.write(infile.read())

def main():
    # Get all Python files in the current directory
    python_files = [file for file in os.listdir() if file.endswith('.py')]

    # Exclude the script file itself from the merge
    script_file = os.path.basename(__file__)
    input_files = [file for file in python_files if file != script_file]

    # Specify the output file name
    output_file = 'merged.py'

    # Merge the files
    merge_files(output_file, *input_files)
    print(f"Successfully merged files into {output_file}.")

if __name__ == '__main__':
    main()
