# CSVFilter
# Language: Python
# Input: TXT
# Output: CSV (filtered data)
# Tested with: PluMA 1.1, Python 3.6
# Dependency: numpy==1.16.0

A PluMA plugin that accepts as input a TXT file of tab-delimited 
keyword-value pairs.  Keywords:

csvfile: CSV file of data, where
rows contain samples and columns represent variable values within
those samples.
threshold: Threshold percentage to keep (between 0 and 1)

Its output file will be the equivalent CSV file with all variables
that have non-zero value across (threshold)% or less of the samples removed.

This is useful particularly when studying a subset of samples with
a specific property.
