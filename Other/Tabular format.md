You have an array of numbers and you would like to print these numbers in a tabular format to make them look more organized.
Eace chell of the table contains exactly one number and is surrounded by exactly four edges:

+-+
|4|
+-+

+-----+
|12345|
+-----+

As you can see above, each corner of the cell is represented by a "+" sign, vertical edges by "-" signs and horizontal edges by "|" signs.
The width of the cell adjusts to accommodate the number of digits of the number written within it. There can be many cells in a row.
Adjacent cells share an edge:

+---+---+---+---+
|  4| 35| 80|123|
+---+---+---+---+

Note, that each cell has the same width. The width of the cell adjusts to math the width of the longest numbers in the table. Example of multi-dimensional array:

+-----+-----+-----+-----+
|    4|   35|   80|  123|
+-----+-----+-----+-----+
|12345|   44|    8|    5|
+-----+-----+-----+-----+
|   24|    3|   22|   35|
+-----+-----+-----+-----+

Write function:
def solution(A, N, K)

where:
A - array
N - number of rows
K - array's length

The function should not return any value.

Assume that:
- N is an integer within the range [1...200]
- K is an integer within the range [1...1,000,000,000]
- each element of array A is an integer within the range [0...1,000,000,000]
