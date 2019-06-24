
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



B = [1,2,-3,6,4,-2,-1]

# print(solution(B))

# ------------------------------------------------
# Here is another solution that I found here:
A = [1,2,3,6,4,2,1]

def solution2(A):
    print(f"A befor sorting is = {A}")
    A = sorted(A)
    print(f"A after sorting is = {A}")

print(10*"--","Sort and Sorted",10*"--")
A.sort()
sortedA = [item for item in A]
sortedAplus = [item for item in sorted(A)]

solution2(A)

print(max(A),min(A))
print(A)
print(sortedA)
print(sortedAplus)
