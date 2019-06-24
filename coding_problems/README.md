# A Collection of Several programming puzzles and challenges
Here i have collected several coding puzzles and ideas that I found them interesting.

## P1- Find the smallest integer not in a list.
If the data structure can be mutated in place and supports random access then you can do it in O(N) time and O(1) additional space. Just go through the array sequentially and for every index write the value at the index to the index specified by value, recursively placing any value at that location to its place and throwing away values > N. Then go again through the array looking for the spot where value doesn't match the index - that's the smallest value not in the array. This results in at most 3N comparisons and only uses a few values worth of temporary space.
read more here:https://stackoverflow.com/questions/1586858/find-the-smallest-integer-not-in-a-list

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
## P2- Compare two consecutive items in a list
More details are found here
https://stackoverflow.com/questions/24577688/compare-current-item-to-next-item-in-a-python-list

```py
mylist = [1, 2, 2, 4, 2, 3]
for i, j in enumerate(mylist[:-1]):
    if j  == mylist[i+1]:
        mylist[i] = "foo"
        mylist[i+1] = "foo"
print (mylist)
[1, 'foo', 'foo', 4, 2, 3]

j = 1
compare = [1,2,5,3,2,4,4,2,6]
for item in compare:
    print(item,compare[j])
    j +=1
```

## P3 -
