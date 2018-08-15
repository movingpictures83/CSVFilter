# CSVFilter
# Language: Python
# Input: CSV (file to filter)
# Output: CSV (filtered data)
# Tested with: PluMA 1.0, Python 2.7

A PluMA plugin that accepts as input a CSV file of data, where
rows contain samples and columns represent variable values within
those samples.

Its output file will be the equivalent CSV file with all variables
that have zero value across all samples removed.

This is useful particularly when studying a subset of samples with
a specific property.
