# Importing io library
import io
import pandas as pd
import numpy as np

# Read files to dataframes
df1 = pd.read_csv('Input_files/input1.bed', sep='\t',header=None)
df2 = pd.read_csv('Input_files/input2.bed', sep='\t',header=None)


# Add headers
df1.columns = ['chromosome', 'start', 'stop', 'name', 'score', 'strand']
df2.columns = ['chromosome', 'start', 'stop', 'name', 'score', 'strand']

# Convert into numpy array
df1 = df1.to_numpy()
df2 = df2.to_numpy()

# Checking whether the properties are satisfied
rows = []
for i in range(len(df1)):
    for j in range(len(df2)):
        # Check for chromosome
        if (df1[i][0]==df2[j][0]):
            # Check whether 1000 basepairs apart
            if (abs(int(df1[i][1])- int(df2[j][2]))<=1000) or (abs(int(df2[j][1])- int(df1[i][2]))<=1000):
                rows.append(df1[i])
                rows.append(df2[j])

# Writing to the file using pandas dataframe
path = "Output_files/prob2_output.bed"
df = pd.DataFrame(rows)
df.to_csv(path, header=None, sep='\t', index=False)