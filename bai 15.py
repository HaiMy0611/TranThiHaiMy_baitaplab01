a = float(input("Nhap so a: "))
b = float(input("Nhap so b: "))
x= ((a+b)/(a**(1/3)+b**(1/3)))-((a*b)**(1/3))
y= ((a**(1/3))-(b**(1/3)))**2
print("Ket qua bieu thuc la: ",x/y)