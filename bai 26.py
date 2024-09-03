#caua
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b < c:
    b, c = c, b
print("Các số theo thứ tự tăng dần là: ",c,"<",b,"<",a)
#caub
N = int(input("Nhập số nguyên N= "))

x = N // 1000       
y = (N % 1000) //100  
z = (N % 1000) %100//10 
t = N%10        

if x > y :
    x, y = x, y
if x > z:
    x, z = z, x
if x > t:
    x, t = x, t
if y > z:
    y, z = z, y 
if y > t:
    y, t = t, 
if z > t:
    z, t = t, z 

Ket_qua_tang_dan = x * 1000 + y * 100 + z*10+ t

print("Số có các chữ số theo thứ tự tăng dần là: ", Ket_qua_tang_dan)
