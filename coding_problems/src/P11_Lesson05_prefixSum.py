'''
Write a function:

    int solution(int A, int B, int K);

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

    { i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Assume that:

        A and B are integers within the range [0..2,000,000,000];
        K is an integer within the range [1..2,000,000,000];
        A ≤ B.

Complexity:

        expected worst-case time complexity is O(1);
        expected worst-case space complexity is O(1).
'''

counter = 0
A = 6
B = 20
K = 3
domain = B- A
print(A,B,domain)

for i in range(A,B,1):
    if i % K == 0:
        counter = counter+1
    else:
        continue
print(counter)

# The solution that I found
remainderA = A % K
print(remainderA)
if remainderA:
    A = A+(K-remainderA)
if A > B:
    print(0)
print(int(((B-A)/K)+1))
