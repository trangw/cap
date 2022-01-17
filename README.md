# Prompt

Imagine you are working on software that allows you to build and maintain
commission plans, and one of your customers asked you to build a new feature to
be used for reporting purposes.

The data is stored in a structured format, and example inputs will be provided
to you below.

Your task is to build a program that provides a way for the customer to group
records by given columns, and run aggregations (count, sum, average) around
them. If you are familiar with SQL, this is similar to the GROUP BY
functionality.

# Deliverables

Please submit a program in any programming language of your choice that meets
the following specifications and submit a brief (1-3 paragraphs) written
summary of some design decisions you made while implementing your solution.

# Specifications

## Execution

Your program should be executable and take in the path to a CSV file as an
argument. If there are any additional steps required to compile your solution,
please indicate which steps are required to compile the solution in the brief.

Python example: `python mysolution.py inputfile.csv`
Node example: `node mysolution.js inputfile.csv`

## Input

The input to your program will be a CSV file containing at least 3 lines.

The first line of the input CSV file will be the comma-separated list of
columns that defines the grouping.

The second line of the input CSV file will be the comma-separated list of
aggregations to be computed. The aggregations will always come in pairs with
the aggregation function coming first, followed by the column to be aggregated.

The third line of the input CSV file will be the start of the CSV file which
represents the input data.

In the four example inputs and outputs presented below, the input data will be
from the same example:

id | name  | deal_size | month    
---|-------|-----------|----------
1  | John  | 100       | October  
2  | Anna  | 100       | October  
3  | John  | 200       | November 
4  | Danny | 50        | October  
5  | Jaime | 100       | November 
6  | Anna  | 100       | October  

## Output

The output of your program should be a CSV file containing the columns which
are grouped and the desired aggregations per the input written to the standard
output (stdout).

In your program's output, the columns do not need to follow any particular
order, although each record should present the values of the columns in the
same order that the columns are initially presented.

In your program's output, the records do not need to be presented in any
particular order.

### Example 1

Input:
```
month
count,id
id,name,deal_size,month
1,John,100,October
2,Anna,100,October
3,John,200,November
4,Danny,50,October
5,Jaime,100,November
6,Anna,100,October 
```

Output:
```
month,count(id)
October,4
November,2
```

### Example 2

Input:
```
name,month
sum,deal_size
id,name,deal_size,month
1,John,100,October
2,Anna,100,October
3,John,200,November
4,Danny,50,October
5,Jaime,100,November
6,Anna,100,October 
```

Output:
```
name,month,sum(deal_size)
John,October,100
Anna,October,200
John,November,200
Danny,October,50
Jaime,November,100
```

### Example 3

Input:
```
name
sum,deal_size,average,deal_size
id,name,deal_size,month
1,John,100,October
2,Anna,100,October
3,John,200,November
4,Danny,50,October
5,Jaime,100,November
6,Anna,100,October 
```

Output:
```
name,sum(deal_size),average(deal_size)
John,300,150
Anna,200,100
Danny,50,50
Jaime,100,100
```

### Example 4

Input:
```
deal_size,name
count,id
id,name,deal_size,month
1,John,100,October
2,Anna,100,October
3,John,200,November
4,Danny,50,October
5,Jaime,100,November
6,Anna,100,October 
```

Output:
```
deal_size,name,count(id)
100,John,1
100,Anna,2
200,John,1
50,Danny,1
100,Jaime,1
