# Here we will follow the codility-lesson-solutions given here:
#https://github.com/ghanan94/codility-lesson-solutions
# Download the answers as "git clone https://github.com/ghanan94/codility-lesson-solutions.git"

A = [3, 8, 9, 7, 6]

k = 2
Axis_of_rotation = len(A)-k
# for index, item in enumerate(A):
#     print(index,item)

# for i in range(Axis_of_rotation):
#     print(A[i])
L1 = A[:2]
L2 = A[len(L1):-1]

print(A)
print(L1)
print(L2)

def rotate(l, n):
    return l[:-n] + l[-n:]

print(rotate(A,2))


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


