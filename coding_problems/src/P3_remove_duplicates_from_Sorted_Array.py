# Task No. 1
# Remove duplicates from a sorted Array


A = [1,1,2,3,3,3,2,5,5,5,112,121,323,323,2323,2322,222,222]

Duplicates = []

j = 1
for i in range(len(A)):
    if j < len(A):
        if A[i]==A[j]:
            Duplicates.append(A[i])
    j = j+1

Duplicates2 = []
checklist = []
count =[]
dicA = {}
counter = 0
for i in range(len(A)):
    counter = 0
    for j in range(len(A)):
        if i != j:
            if A[i] == A[j]:
                counter = counter + 1
                count.append(counter)
                checklist.append(A[j])
                if A[j] not in Duplicates2:

                    Duplicates2.append(A[i])




#print(Duplicates)
print(A)
print(Duplicates2)
print(checklist)
print(count)
print(dicA)
#print(dicA)

#print(A.count(Duplicates2[2]))
# listofstr = ["column1", 'column1', 'column3']
# dictx = {}
# for i in listofstr:
#     dictx[i] = listofstr

# print(dictx)

