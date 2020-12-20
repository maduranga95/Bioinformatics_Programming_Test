# Needed imports 
import csv
from collections.abc import Iterable
import pandas as pd

# Function to flatten a 2D list
def flatten(l):
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el
# Reading expression file
expression_df = pd.read_csv('Input_files/GSE47438.csv', sep=',')

# Save header for later writing to output file
headers = list(expression_df.columns)

# Remove header from data
expression_df = expression_df[:].values

# Initialize empty dictionary to insert probe id as key and value_list as value
expression_file_data_with_values ={}
for row in expression_df:
    
    temp = list(map(float, row[1:]))
    expression_file_data_with_values[row[0]]= temp

# Read platform file (Downloaded as .txt file)
# List of objects with probe as key and symbol as value
platform_file_data = []
platform_df = pd.read_csv('Input_files/GPL6947-13512.txt', sep='\t', skiprows=30)
lines = platform_df.to_numpy()
for line in lines:
    probe_symbol_object = {}
    probe_symbol_object['probe'] = line[0]
    probe_symbol_object['symbol'] = line[13]
    platform_file_data.append(probe_symbol_object)      

# Get an object with symbol as key and relevant probe ids list as value
symbol_probe = {}
for item in platform_file_data[1:]:
    symbol_probe.setdefault(item['symbol'], []).append(item["probe"])

# Iterate through each symbol and their respective probe id list to get the expression values (and the max of their sums)
write_list = []
for symbol in symbol_probe.keys():
    # Check whether the symbol is empty
    if not pd.isnull(symbol):
        row_list =[]
        sum_obj = {}
        for probe in symbol_probe[symbol]:
            if probe in expression_file_data_with_values.keys():
                sum_value = sum(expression_file_data_with_values[probe])
                sum_obj[probe] = sum_value
            else:
                continue
        
        # Get the probe id that has max sum of expression data
        max_probe = max(sum_obj, key=sum_obj.get)
        # Prepare writing row
        row_list.append(symbol)
        row_list.append(expression_file_data_with_values[max_probe])
        # Flatten the expression value list
        flat_list = list(flatten(row_list))
        # Append to create final writing 2D list
        write_list.append(flat_list)
    else:
        continue

# Add headers to the csv data
write_list.insert(0, headers) 

# Write to the output CSV file using the 2D list
path = "Output_files/prob3_output.csv"
df = pd.DataFrame(write_list)
df.to_csv(path, index=False, header=None)


