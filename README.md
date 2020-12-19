# Bioinformatics Programming Test 

The following programming test is meant to be conducted in the Python language, using the standard libraries. The expected deliverables are Python scripts that could be run from the command line on a regular Unix station. The face-to-face portion of the test consists of going over the scripts line by line via screen sharing in a zoom call. I expect the code to be documented via comments, so potentially another programmer could build on it. 

**Problem 1.** In genomics data, we usually deal with large text files containing chromosome
locations. An example is the BED file format, defined at

http://genome.ucsc.edu/FAQ/FAQformat.html#format1

As an example, you might get a TAB-delimited text file containing lines such as

chr1    3   10  one 1   + \
chr2    4   5   two 1   + \
chr2    1000    2000    three   1   + 


with the following fields
* chromosome
* start
* stop
* name of the read/annotation/feature
* a score (or 1 if the score is not important)
* strand (+/-)

You need to produce a script that takes as input a file like the one above, and splits it into
a number of files such as all entries in one file belong to the same chromosome.

Hints: file handles, hash

**Problem 2.** Next, we receive as input two bed file like the one above,
with the property that the names in both files are matching,
but not the genomic coordinates.

**a)** Produce a script that takes as input the BED files and determines
all reads that have the following property
* have mappings in both files on the same chromosome
* the mappings are no longer that 1000 basepairs apart

For example

File 1: \
chr1    3   10  one 1   + \
chr2    4   5   two 1   + \
chr2    1000    2000    three   1   +  

File 2: \
chr7    3   10  one 1   + \
chr2    450   700   two 1   + \
chr2    11000    12000    three   1   + 

The only read that passes is "two". Read "one" has the ends mapping on different chromosomes,
while "three" has the ends about 10,000 base pairs apart, which exceeds 1000.

**b)** Assume we have at our disposal multiple computers, and our input BED files are really big.
Is there a way to combine what you have done at 1) with 2a) to speed up the process ?

------
Notes:\
**1.** Please provide test examples for both 1) and 2) I want to see 3 example sizes for each 

* small: BED file(s) with less than 50 entries
* medium: BED file(s) with ~ 1,000 entries
* large: BED file(s) with ~100,000 entries
[you can use the attached input and output .bed files to test your code]

**2.** As a good practice, please insert comments in your code to make it
more readable, but also easy to execute/maintain/develop by somebody else than
yourself.
-----

**Problem 3.** Please download GPL6947-xxx.txt, the platform of microarray at
https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GPL6947
Click Download Full Table to retrieve it.[located near the end of the web page]

Attached in this repo is GSE47438.csv, the microarray expression data. Please write a Python program to read in both platform file and the expression data file and convert the expression data from probe id based to gene symbol based. If there are multiple rows with the same gene symbol, select the one whose sum across the row is greatest and discard the rest.  Output the result to a new csv file.
