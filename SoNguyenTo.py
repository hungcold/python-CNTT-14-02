def Songuyento(n):
    if(n<2):
        return False
    i=2;
    while i <= n/2:
        if(n%i == 0):
            return False
        i+=1
    return True
n = int(input("Nhap 1 so:"))
check = Songuyento(n);
if check == 1:
    print(n, "la 1 so nguyen to")
else:
    print(n, "khong phai 1 so nguyen to")
