# Task No. 1
# Remove duplicates from a sorted Array

from collections import Counter

A = [1,1,2,3,3,3,2,5,5,5,112,121,323,323,2323,2322,222,222]

Duplicates = []

j = 1
for i in range(len(A)):
    if j < len(A):
        if A[i]==A[j]:
            Duplicates.append(A[i])
    j = j+1
# ----------------------------------------------------------------
A = [1,2,2,2,3,3,3,3,5,5,5,5,5,5,]
Duplicates2 = []
checklist = []
count =[]
dicA = {}
c = 0
name = ""
dictCount = {}
dictCount2 = {}
for i in range(len(A)):
    for j in range(len(A)):
        if i != j:
            if A[i] == A[j]:
                name = A[j]
                checklist.append(A[j])
                if A[j] not in Duplicates2:
                    dictCount[str(name)] = 1
                    Duplicates2.append(A[i])
                else:
                    continue
                dictCount[str(name)]= dictCount[str(name)] +1

print(dict((i, A.count(i)) for i in set(A)))
# ----------------------------------------------------------------
def occur_dict(a):
    d = {}
    for i in a:
        if i in d:
            d[i] = d[i]+1
        else:
            d[i] = 1
    return d
# ----------------------------------------------------------------
#print(Duplicates)
print(A)
print(Duplicates2)
print(checklist)
print(count)
print(dictCount)
print(occur_dict(A))
# print(dicA)
# #print(dicA)
# print(Counter(A))
#print(A.count(Duplicates2[2]))
# listofstr = ["column1", 'column1', 'column3']
# dictx = {}
# for i in listofstr:
#     dictx[i] = listofstr

# print(dictx)

def count_duplicates2(seq):

    '''takes as argument a sequence and
    returns the number of duplicate elements'''

    counter = 0
    countlist = []
    seen = set()
    for elm in seq:
        if elm in seen:
            counter += 1
            countlist.append(counter)
        else:
            seen.add(elm)
            counter = 1

    return counter, seen, countlist

print(10*"=","Here we will test another function")
listA = ["apple","apple","google","apple","google","IBM","TOYOTA","NISSAN","TESLA","TESLA"]
print(listA)
print(count_duplicates2(listA))



def count_duplicates(seq):
    fir = 0
    sec = 0
    count = 0
    duplicates=[]
    print ("Pairs of duplicates: ")
    while fir < len(seq):
        while sec < len(seq):
            if fir < sec and seq[fir] == seq[sec] and seq[fir] not in duplicates:
                count += 1
                print(fir, sec)
            sec += 1
        duplicates.append(seq[fir])
        fir += 1
        sec = 0
    return count
c=count_duplicates(listA)
print ("Number of duplicates: ",c)
