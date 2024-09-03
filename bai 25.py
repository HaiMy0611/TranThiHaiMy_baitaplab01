chu = input("Nhap mot chu: ")
if chu.isupper():
    print("Chu thuong tuong ung la: ", chu.lower())
elif chu.islower():
    print("Chu hoa tuong ung la: ", chu.upper())
else:
    print("Vui long nhap lai")
    
