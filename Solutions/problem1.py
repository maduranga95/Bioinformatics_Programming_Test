# Importing io library
import io
import pandas

# Read file to dataframe
try:
    df = pandas.read_csv('Input_files/testcasde_100000_1.bed', sep='\t',header=None)

    # Add Column headers
    df.columns = ['chromosome', 'start', 'stop', 'name', 'score', 'strand']

    # Group by chromosome and write to seperate files
    for i, g in df.groupby(['chromosome']):
        path = "Output_files/output_" + i+ ".bed"
        g.to_csv(path, header=None, sep='\t')
except (FileNotFoundError, IOError):
    print("File not found.")
    
