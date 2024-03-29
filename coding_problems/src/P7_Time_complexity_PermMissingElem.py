'''
A zero-indexed array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given a zero-indexed array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Assume that:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
'''

A = [4,3,1,5]

missing_element = 0
for i in range(max(A)+1):
    if i not in A:
        missing_element = i

print(missing_element)

print(max(A))


#Code written in Python
#Correctness: 100 %
#Performance: 100 %
#Time Complexity: O(N)
#Space Complexity: O(1)

def solution(A):
    N = len(A) + 1
    missing = ((N + 1) * N) / 2

    for x in A:
        missing -= x

    return missing

print(solution(A))
