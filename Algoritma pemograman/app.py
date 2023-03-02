# #1 type data

# ''' 
# Tipe Data Boolean 
# simpan dengan nama boolean.py 
# ''' 
# narkoba = False 
# belajar = True 
 
# print(narkoba) 
# print(belajar)  


# ''' 1.2 string_fotmat.py
# String Format simpan dengan nama string_format.py Contoh :''' 

# first_name = "Rofi'ah" 
# middle_name = "Azwa" 
# last_name = "Nisrina" 
 
# print(f"Halo nama saya {first_name} {middle_name} {last_name}") 


# print('-------------------------------------------')
# #2 variabel
# '''2.1 buatlah program menggunakan variabel,dengan variabel yang mendeskripsikan biodata anda'''

# # biodata
# print("bodata")
# deskripsi ="ini program python"
# nama = "Rofi'ah Azwa NIsrina" 
# alamat = "Aimas.Jln.Klamono km 20" 
# umur = "17"
# hobi = "menggambar" 

# print(f"nama saya {nama},yang beramat di {alamat},umur sekarang {umur} tahun,dan memiliki hobi {hobi}")

# '''2.2  menghitung luas & keliling persegi panjang'''

# print('2.2  menghitung luas & keliling persegi panjang')
# panjang = 15 
# lebar = 5.7
# luas_persegi_panjang = panjang * lebar
# keliling_persegi_panjang = 2 * (panjang + lebar)

# print(f"sebuah persegi panjang memiliki panjang {panjang} cm,lebar {lebar} cm,dan memiliki luas sebesar {luas_persegi_panjang} cm,dan keliling {keliling_persegi_panjang} cm")

# print('---------------------------------------------')
# #3 operator

# '''3.1menghitung luas bangun datar'''
# print("3.1 menghitung luas bangun datar")

# #menghitung persegi panjang
# print("/n====menghitung persegi panjang====")
# panjang = 50
# print("panjang :",panjang)
# lebar = 25.5
# print("lebar :",lebar)
# luas = panjang * lebar
# print("luas :",luas)

# #menghitung persegi
# print("/n====menghitung persegi====")
# sisi = 20
# print("sisi :",sisi)
# luas = sisi * sisi
# print ("luas :",luas)

# #menghitung segitiga
# print("/n====menghitung segitiga====")
# alas = 40
# print("alas :",alas)
# tinggi = 60
# print("tinggi :",tinggi)
# luas = 0.5 * alas * tinggi 
# print ("luas :",luas)

# #menghitung lingkaran
# print("/n====menghitung lingkaran====")
# phy  = 3.14
# print("phy: ",phy)
# diameter = 14
# print("diameter :",diameter)

# #proses pertama
# r = int(diameter) / 2

# #output
# print ("Jari-jarinya: ", r)

# #proses kedua
# luas = float (phy) * int (r) * int (r)

# #output
# print ("luas :",luas)

# #menghitung jajargenjang
# print("/n====menghitung jajargenjang====")
# alas = 5
# print("alas :",alas)
# tinggi = 14
# print("tinggi :",tinggi)
# luas = alas * tinggi
# print("luas :",luas)

# #menghitung trapesium
# print("/n====menghitung trapesium====")
# a = 10
# print("a :",a)
# b = 16
# print("b :",b)
# tinggi = 8
# print("tinggi :",tinggi)
# luas =(a + b) * tinggi / 2
# print("luas :",luas)

# '''3.2 buatlah program nya dengan output seperti pada gambar di bawah,gunakan operator bitwise,dengan menentukan 
# berapakah nilai variabel a, b dengan nilai output seperti pada gambar'''

# print("3.2 buatlah program nya dengan output seperti pada gambar di bawah, gunakan operator bitwise")

# # soal
# a = 9
# b = 4

# c = a & b
# d = a | b 
# e = ~a 
# f = a ^ b 

# #hsil
# print("/n hasil")
# print(f"a & b = {c}")
# print(f"a | b = {d}")
# print(f"~a = {e}")
# print(f"a ^ b = {f}")


# a = 3
# print(f"isi variabel a:%d /n",a)
# print(f"isi variabel a:",a)


# tugas_laporan_ke = 10

# a.Program menampilkan nilai faktorial dari angka yang di input.
#input angka
# print('##  Program Python nilai faktorial  ##')
# print()

# a = int (input("masukkan angka: "))
# faktorial = 1

# #nilai faktor angka
# for a in range(1, a + 1):
#     faktorial *= a
# print(f'faktor dari {a} adalah = {faktorial}')


# # b.Program menampilkan karakter dari string upper case dan lower case pada sebuah string
# print()
# print('##  Program Python string upper dan lower  ##')
# print()

# def menghitung_kasus(string):
#     hitung_upper = 0
#     hitung_lower = 0
#     for karakter in string:
#         if karakter.isupper():
#             hitung_upper+=1
#         elif karakter.islower():
#             hitung_lower +=1

#     print("jumlah karakter upper case pada string =", hitung_upper)
#     print("jumlah karakter lower case pada string =", hitung_lower)

# string = str(input("masukkan string original : "))
# menghitung_kasus(string)


# # c.Program yang menampilkan segitiga pascal dari input angka
# print()
# print('##  Program Python Segitiga pascal  ##')
# print()

# def segita_pascal(ukuran):
#     for i in range(0, ukuran):
#         for j in range(0, i + 1):
#             print(putuskan_nomor(i, j), end=" ")
#         print()

# def putuskan_nomor(n, k):
#     angka = 1
#     if k > n - k:
#         k = n - k
#     for i in range(0, k):
#         angka = angka * (n - i)
#         angka = angka // (i + 1)
#     return angka

# jumlah_baris = int(input("Masukan angka :"))
# segita_pascal(jumlah_baris)

# d. program yang menampilkan list angka yang dikalikan dengan angka itu sendiri.
# print()
# print('##  Program Python pengalian list angka  ##')
# print()

def list():
    
    x = int (input("masukkan angka pertama :"))
    y = int (input("masukkan angka akhir :"))
    hasil = []
    for i in range(0, y):
        h = x*x
        hasil.append(h)
        x+=1
    print(hasil)
list()

        
