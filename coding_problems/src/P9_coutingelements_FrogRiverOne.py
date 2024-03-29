'''
A small frog wants to get to the other side of a river. The frog is currently located at position 0, and wants to get to position X. Leaves fall from a tree onto the surface of the river.

You are given a non-empty zero-indexed array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X. You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4

In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:

    int solution(int X, vector<int> &A);

that, given a non-empty zero-indexed array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4

the function should return 6, as explained above.

Assume that:

        N and X are integers within the range [1..100,000];
        each element of array A is an integer within the range [1..X].

Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(X), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.
'''

A = [1,3,1,4,2,3,5,4,3,3,6]

X = 8
time_to_arrive = 0
sorteddistance = sorted(A)
A_unique = set(A)
for time, position in enumerate(sorteddistance):
    #print(time, position)
    if position == max(A_unique):
        print(time-1)

print(10*"-","Solution using python by converting a CPP solution",10*"-")
# for position in A_unique:
#     print(position)

# print(A_unique)

# print(sorteddistance)

# int solution(int X, vector<int> &A) {
#     bool landed[X];

#     for (int i = 0; i < X; i++) {
#         landed[i] = false;
#     }

#     for(int i = 0; i < A.size(); i++) {
#         if (!landed[A[i] - 1]) {
#             landed[A[i] - 1] = true;

#             if (--X == 0) {
#                 return i;
#             }
#         }
#     }

#     return -1;
# }

landed = []
for i in range(X+1):
    if i < X:
        landed.append("false")
    else:
        landed.append("true")
for i in range(len(A)):
    if not landed[A[i]-1]:
        landed[A[i]-1] = "True"
        X = X-1
        if X == 0:
            print(i)

print(landed)
