A non-empty array A consisting of N real numbers is given. A slice of the array is a pair of integers (P,Q) such that 0≤P≤Q<N. The number A[P]*A[P+1]*...*A[Q-1]*A[Q] is called the product of the slice.

For example, consider the following array A:
A[0] = 1.0
A[1] = 0.1
A[2] = -1.0
A[3] = -7.0
A[4] = 3.0
A[5] = -5.0
A[6] = -2.5
A[7] = 0.0
A[8] = 1.0

Pair (2,4) is a slice of array A with product 21.0.
Pair (1,3) is a slice of array A with product 0.7.
Pair (3,5) is a slice of array A with product 105.
Pair (2,6) is a slice of array A with product 262.5.
No slice of array A has a greater product than 262.5.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N real numbers, returns the maximum product of any slice of array A. If the maximum product is greater than 1,000,000,000.0, the function should return 1,000,000,000.0.

For example, given array A such that:\
A[0] = 1.0
A[1] = 0.1
A[2] = -1.0
A[3] = -7.0
A[4] = 3.0
A[5] = -5.0
A[6] = -2.5
A[7] = 0.0
A[8] = 1.0

the function should return 262.5, as explained above.

Assume that:
- N is an integer within the range [1...100,000];
- each element of array A is a real number within the range [-10,000.0...10,000.0]

Complexity:
- expected worst-case time complexity is O(N)
- expected worst-case space complexity is O(1) (not counting the storage required for input arguments)
