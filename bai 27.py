import math 

hinh = input ("Nhap chu: ")
if hinh == 'v':
    print("Tinh P va S cua hinh vuong")
    canh = float(input("Nhap do dai canh hình vuông: "))
    Chu_vi = canh*4
    Dien_tich = canh*canh
    print ("P =", Chu_vi, "S=", Dien_tich)
elif hinh == 'n':
    print("Tinh P va S cua hinh chu nhat")
    chieu_rong = float(input("Nhap chieu rong cua hinh chu nhat: "))
    chieu_dai = float(input("Nhap chieu dai cua hinh chu nhat: "))
    Chu_vi_hcn = 2*(chieu_rong+chieu_dai)
    Dien_tich_hcn = chieu_dai*chieu_rong
    print("P=", Chu_vi_hcn, "S", Dien_tich_hcn)
elif hinh == 't':
    print("Tinh P va S cua hinh tron")
    ban_kinh = float(input("Nhap ban kinh cua hinh tron:"))
    Chu_vi_htron = 2*math.pi*ban_kinh
    Dien_tich_htron = math.pi*(ban_kinh**2)
    print("P=", Chu_vi_htron,"S=", Dien_tich_htron)
else:
    print("Vui long nhap lai")
    
    