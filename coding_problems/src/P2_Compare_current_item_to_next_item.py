# More details overthis issue can be found here
#https://stackoverflow.com/questions/24577688/compare-current-item-to-next-item-in-a-python-list

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
    if j == len(compare):
        break
    print(item,compare[j])
    j +=1


