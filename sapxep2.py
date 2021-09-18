def sapxep(list):
    for i in range(0, list - 1):
        for j in range(i + 1, list):
            if(list[i] > list[j]):
                list[i] = temp
                list[i] = list[j]
                temp = list[j]

check = input().split()

while len(check) == 0:
    if len(check) == 0:
        print("Danh sách rỗng hãy nhập lại!")
    else:
        try:
            list = list(map(int, check))
            sapxep(list)
            print(*list)
        except:
            print("Vui lòng nhập số thực!")



