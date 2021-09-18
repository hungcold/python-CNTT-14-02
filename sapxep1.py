list = [5,9,8,7,4,2,1,3]
numer = len(list)
for i in range(0, numer -1):
    for j in range(i + 1, numer):
        if(list[i] > list[j]):
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
print(list)