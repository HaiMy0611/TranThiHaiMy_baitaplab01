a = int(input("Nhập số nguyên thứ a: "))
b = int(input("Nhập số nguyên thứ b: "))
c = int(input("Nhập số nguyên thứ c: "))
d = int(input("Nhập số nguyên thứ d: "))
S = a
if b < S:
    S = b
if c < S:
    S = c
if d < S:
    S = d  
print("Số nhỏ nhất là: ",S)