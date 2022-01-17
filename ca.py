#################################################################################################
# Filename: c.py
# Version:  python 3.8
# Execution: `python c.py filename.csv`
# Purpose:  Reads input from given csv file,  group records by given columns, 
#           and run aggregations (count, sum, average) around them. 
#################################################################################################
# Input:
# The input to your program will be a CSV file containing at least 3 lines.
# 1 The first line of the input CSV file will be the comma-separated list of columns that defines the 
#   grouping.
# 2 The second line of the input CSV file will be the comma-separated list of aggregations to be computed. 
#   The aggregations will always come in pairs with the aggregation function coming first, followed by the 
#   column to be aggregated.
# 3  The third line of the input CSV file will be the start of the CSV file which represents the input data.
#
# Output:
# The output of your program should be a CSV file containing the columns which are grouped and the desired 
# aggregations per the input written to the standard output (stdout). The columns do not need to follow any 
# particular order, although each record should present the values of the columns in the same order that 
# the columns are initially presented.
#
# Approach Summary:
# The tuple approach applies one aggregation at a time to a column. The resultant column needs to be renamed 
# after each aggregation. Alternatively, another appraoch would be to use a dictionary for the agg method, but
# we need to be able to change the column name, the tuple approach, while may not seem as optimal, is prefered.
#
# Here, I also chose to use pands dataframe and the aggregation functions in pandas for ease of data manipulation. 
# However, I could use the statistical functions from scipy or numpy,  but the use cases (type of data domain) 
# for these libraries do not justify nor seem beneficial and would add complexity to the code.
#
#################################################################################################
import csv
import pandas as pd
#file='filename3.csv'
file=input('Please enter a csv file name: ')
with open(file, newline='') as f:
  reader = csv.reader(f)
  row1 = next(reader)  # gets the first line
  row2 = next(reader)
  df = pd.read_csv(file,skiprows=2,header=0)
data=pd.DataFrame()
for i in range(len(row2)//2):
  ag=row2.pop(0)
  col=row2.pop(0)
  if ag=='average' : ag='mean'
  data=pd.concat([data,df.groupby(row1).agg(new=(col,ag)).rename(columns={'new':ag+'_'+col})],axis=1)
print(data)
data.to_csv('output.csv')