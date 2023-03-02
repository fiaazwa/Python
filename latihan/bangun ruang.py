#menghitung volume kubus
sisi=input("masukkan sisi")

#proses
volume=int(sisi)**3

#output
print (volume)

#menghitung lingkaran
phy  = 3.14
diameter = input ("masukkan nilai diameter: ")

#proses pertama
r = int (diameter) / 2

#output
print ("Jari-jarinya: ", r)

#proses kedua
luas = float (phy) * int (r) * int (r)

#output
print (luas)

#menghitung persegi sama kaki
alas = input ("masukkan alas")
tinggi = input ("masukkan tinggi")
dua = input ("masukkan dua")

#proses
luas = int(alas) * int(tinggi) / int(dua)
 
#output
print (luas)

#menghitung persegi panjang
panjang = input("masukkan panjang")
lebar = input("masukkan lebar")

#proses
luas = int(panjang) * int(lebar)

#output
print(luas)

