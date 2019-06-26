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

## P3 - Rotate a list based on a value:

This is a quesiton from codility as

```v
A zero-indexed array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is also moved to the first place.

For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]. The goal is to rotate array A K times; that is, each element of A will be shifted to the right by K indexes.

Write a function:

struct Results solution(int A[], int N, int K);

that, given a zero-indexed array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given array A = [3, 8, 9, 7, 6] and K = 3, the function should return [9, 7, 6, 3, 8].

Assume that:

N and K are integers within the range [0..100];
each element of array A is an integer within the range [−1,000..1,000].
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
```
## Analyzing
1. step one: think about the output, should be a list with two segments one come from cutting the list in (k) values and rest are the one will be rotated about:

```b
for example:
listX = [a1,a2,a3,a4,a5,a6] and you said k =3
means
[a1,a2] ---> to be think of it as axis of rotation
[a3,a4,a5,a6] ----> the rest of the list to be rotated around
Now we need to figure out the length of each array
first one is: [a1,a2] is k length
second one is: len(listX)-k
then construct your new array based on these values using two for loops.
```
## Output

The solution which is working for now:

```py
# Returns the rotated list
def rightRotate(lists, num):
    output_list = []

    # Will add values from n to the new list
    for item in range(len(lists) - num, len(lists)):
        output_list.append(lists[item])

    # Will add the values before
    # n to the end of new list
    for item in range(0, len(lists) - num):
        output_list.append(lists[item])

    return output_list

print(10*"-")
print(rightRotate(A,3))
```

## P5 - Odd Occurrence in Array

```
A non-empty zero-indexed array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

int solution(int A[], int N);

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Assume that:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
```

# P6 - Time Complexity - FrogJmp
Here is the question

```py

```
