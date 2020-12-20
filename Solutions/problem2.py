# Importing io library
import io
import pandas as pd
import numpy as np

# Binary search and return index of closest value
def find_nearest(array, value):
    array = np.asarray(array)
    index = (np.abs(array - value)).argmin()
    return index

# Read files to dataframes
try:
    initial_df1 = pd.read_csv('Input_files/input1.bed', sep='\t',header=None)
    initial_df2 = pd.read_csv('Input_files/input2.bed', sep='\t',header=None)

    # Add headers
    initial_df1.columns = ['chromosome', 'start', 'stop', 'name', 'score', 'strand']
    initial_df2.columns = ['chromosome', 'start', 'stop', 'name', 'score', 'strand']

    # Sorting for binary search
    df2 = initial_df2.sort_values(by=['start'])
    df4 = initial_df2.sort_values(by=['stop'])

    # Convert into numpy array
    initial_df1 = initial_df1.to_numpy()
    df2 = df2.to_numpy()
    df4 = df4.to_numpy()

    # Efficient method to cross-compare each row in both files
    # Binary Search is used with numpy
    rows = []
    # Iterate through rows in first file
    for i in range(len(initial_df1)):
        # Find row index of the nearest 'stop' value in file2 to the 'start' value of file1
        closest_index_case1 = find_nearest(df4[:,[2]], initial_df1[i][1])
        # Condition of Chromosome similarity
        if (initial_df1[i][0]==df4[closest_index_case1][0]):
            # Condition of 'one region is within 1000bp or less from the end of another region'
            if not ((((int(initial_df1[i][1])> int(df4[closest_index_case1][2]))) and ((int(initial_df1[i][1])- int(df4[closest_index_case1][2]))>1000)) or  ((int(initial_df1[i][1])< int(df4[closest_index_case1][2])) and ((int(df4[closest_index_case1][1])-int(initial_df1[i][1]))>1000))) :
                # Append if above conditions are satisfied
                rows.append(initial_df1[i])
                rows.append(df4[closest_index_case1])
                continue
        # Find row index of the nearest 'start' value in file2 to the 'stop' value of file1
        closest_index_case2 = find_nearest(df2[:,[1]], initial_df1[i][2])
        # Condition of Chromosome similarity
        if (initial_df1[i][0]==df2[closest_index_case2][0]):
            # Condition of 'one region is within 1000bp or less from the end of another region'
            if not (((int(initial_df1[i][2]) < int(df4[closest_index_case2][1])) and (( int(df4[closest_index_case2][1])-int(initial_df1[i][2]))>1000)) or  ((int(df4[closest_index_case2][2])<int(initial_df1[i][1])) and ((int(initial_df1[i][1])- int(df4[closest_index_case2][2]))>1000))) :
                # Append if above conditions are satisfied
                rows.append(initial_df1[i])
                rows.append(df2[closest_index_case2])
                continue

        else:
            continue

    # Writing to the file using pandas dataframe
    path = "Output_files/prob2_output.bed"
    df = pd.DataFrame(rows)
    df.to_csv(path, header=None, sep='\t', index=False)

except (FileNotFoundError, IOError):
    print("File not found.")

# Note : The Final output file contains pairs of rows (one from each file) having mappings in both files on the same chromosome and
#        start of one region is withing 1000bp or less from the end of another region. So when understanding the output file, it 
#        be read pairwise from the beginning.