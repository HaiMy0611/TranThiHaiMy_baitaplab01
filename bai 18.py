print("Gio thu nhat")
a= int(input("Nhap gio: "))
b= int(input("Nhap phut: "))
c= int(input("Nhap giay: "))
print("Gio thu hai")
x= int(input("Nhap gio: "))
y= int(input("Nhap phut: "))
z= int(input("Nhap giay: "))
Giay_tong= (a+x)*60*60+(b+y)*60+(c+z)
print("Tong giay la: ", Giay_tong)
Tong_gio= Giay_tong//3600
Tong_phut= (Giay_tong%3600)//60
Tong_giay= Giay_tong%60
print("Tong cua hai gio la: ", Tong_gio,"gio", Tong_phut,"phut", Tong_giay,"giay")
Giay_cua_gio_dau= a*60*60+b*60+c
Giay_cua_gio_sau= x*60*60+y*60+z
Hieu_giay= Giay_cua_gio_dau-Giay_cua_gio_sau
if Hieu_giay<0:
    Hieu_giay=-(Hieu_giay)
print("Hieu hai gio la:", (Hieu_giay)//3600,"gio", ((Hieu_giay)%3600)//60,"phut", (Hieu_giay)%60,"giay")


