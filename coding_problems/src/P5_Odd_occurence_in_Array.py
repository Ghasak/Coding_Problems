# Here is the question
# https://github.com/ghanan94/codility-lesson-solutions/blob/master/Lesson%2002%20-%20Arrays/OddOccurrencesInArray/task.txt

'''
A[0] = 9  A[1] = 3  A[2] = 9
A[3] = 3  A[4] = 9  A[5] = 7
A[6] = 9
'''
A = [9,3,9,3,9,7,9]
outputlist_odds = []
outputlist_evens = []
for i in range(len(A)):
    if i % 2 != 0:
        print(A[i])
        outputlist_odds.append(A[i])
    else:
        outputlist_evens.append(A[i])

for i in range(len(outputlist_evens)-1):
    if outputlist_evens[i] == outputlist_odds[i]:
        print("Ok")

print(10*"-")
print(outputlist_odds)
print(10*"-")
print(outputlist_evens)



