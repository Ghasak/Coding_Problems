# Collecting Several programming puzzles
Here i have collected several coding puzzles and ideas that I found them interesting.

## C1- Find the smallest integer not in a list.
If the data structure can be mutated in place and supports random access then you can do it in O(N) time and O(1) additional space. Just go through the array sequentially and for every index write the value at the index to the index specified by value, recursively placing any value at that location to its place and throwing away values > N. Then go again through the array looking for the spot where value doesn't match the index - that's the smallest value not in the array. This results in at most 3N comparisons and only uses a few values worth of temporary space.

```py
def solution(A):
    index = 0
    target = []
    A = [x for x in A if x >=0]
    if len(A) ==0:
        return 1
    maxi = max(A)
    if maxi <= len(A):
        maxi = len(A)
    target = ['X' for x in range(maxi+1)]
    for number in A:
        target[number]= number
    count = 1
    while count < maxi+1:
        if target[count] == 'X':
            return count
        count +=1
    return target[count-1] + 1


A = [1,2,3,6,4,2,1]
B = [1,2,-3,6,4,-2,-1]

print(solution(B))

```
