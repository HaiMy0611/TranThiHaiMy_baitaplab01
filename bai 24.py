a= int(input("Nhap gio: "))
b= int(input("Nhap phut: "))
c= int(input("Nhap giay: "))
if 0<=a<=24:
    if 0<=b<=60:
        if 0<=c<=60:
            print("Hop le")
        else:
            print("Khong hop le")
    else:
        print("Khong hop le")
else:
    print("Khong hop le")
    
