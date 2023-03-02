# hari = "senin"

# if hari == "senin":
#     print("saya Masuk kuliah")
# elif hari == "selasa":
#     print("saya Masuk kuliah")
# elif hari == "rabu":
#     print("saya Masuk kuliah")
# elif hari == "kamis":
#     print("saya Masuk kuliah")
# elif hari == "jumat":
#     print("saya Masuk kuliah Dan Ujian")
# elif hari == "sabtu":
#     print("saya Masuk kuliah")
# elif hari == "Minggu":
#     print("saya Masuk kuliah")
# else:
#     print("Jalan")

# #program 1
# sisi_a = int(input("masukkan sisi a: "))
# sisi_b = int(input("masukkan sisi b: "))
# sisi_c = int(input("masukkan sisi c: "))

# # #menentukan jenis segitiga
# if sisi_a == sisi_b and sisi_b == sisi_c:
#     print("segitiga tersebut adalah segitiga sama sisi")
# elif sisi_a == sisi_b or sisi_b == sisi_c or sisi_c == sisi_a:
#     print("segitiga tersebut adalah segitiga sama kaki")
# else:
#     print("segitiga tersebut adalah segitiga sembarang")

# program 2
# menentukan tahun kabisat input user
# tahun = int(input("masukkan tahun lahir anda : "))
# #menentukan tahun kabisat
# if tahun % 40 == 0:
#     print("adalah tahun kabisat")
# elif tahun % 100 == 0:
#     print("bukan tahun kabisat")
# elif tahun % 4 == 0:
#     print("adalah tahun kabisat")
# else:
#     print("bukan tahun kabisat")

# #program 3
#  menentukan zodiak yunani 
# tanggal_lahir = int(input("masukkan tanggal lahir anda : "))
# bulan_lahir = int(input("masukkan bulan lahir anda : "))

# if (tanggal_lahir >= 21 and bulan_lahir == 3) or (tanggal_lahir <= 19 and bulan_lahir == 4):
#     print("zodiak anda adalah aries")
# elif(tanggal_lahir >= 20 and bulan_lahir == 4) or (tanggal_lahir <= 20 and bulan_lahir == 5):
#     print("zodiak anda adalah taurus")
# elif(tanggal_lahir >= 21 and bulan_lahir == 5) or (tanggal_lahir <= 20 and bulan_lahir == 6):
#     print("zodiak anda adalah gemini")
# elif(tanggal_lahir >= 21 and bulan_lahir == 6) or (tanggal_lahir <= 22 and bulan_lahir == 7):
#     print("zodiak anda adalah cancer")
# elif(tanggal_lahir >= 23 and bulan_lahir == 7) or (tanggal_lahir <= 22 and bulan_lahir == 8):
#     print("zodiak anda adalah leo")
# elif(tanggal_lahir >= 23 and bulan_lahir == 8) or (tanggal_lahir <= 22 and bulan_lahir == 9):
#     print("zodiak anda adalah virgo")
# elif(tanggal_lahir >= 23 and bulan_lahir == 9) or (tanggal_lahir <= 22 and bulan_lahir == 10):
#     print("zodiak anda adalah libra")
# elif(tanggal_lahir >= 23 and bulan_lahir == 10) or (tanggal_lahir <= 21 and bulan_lahir == 11):
#     print("zosiak anda adalah scorpio")
# elif(tanggal_lahir >= 22 and bulan_lahir == 11) or (tanggal_lahir <= 21 and bulan_lahir == 12):
#     print("zodiak anda adalah sagitarius")
# elif(tanggal_lahir >= 22 and bulan_lahir == 12) or (tanggal_lahir <= 19 and bulan_lahir == 1):
#     print("zodiak anda adalah capricorn")
# elif(tanggal_lahir >= 20 and bulan_lahir == 1) or (tanggal_lahir <= 18 and bulan_lahir == 2):
#     print("zodiak anda adalah aquarius")
# elif(tanggal_lahir >= 19 and bulan_lahir == 2) or (tanggal_lahir <= 20 and bulan_lahir == 3):
#     print("zodiak anda adalah pisces")
# else:
#     print("data yang di masukkan tidak valid")

#program 4
# menentukan zodiak cina sesuai tahun kelahiran
tahun = int(input("masukkan tahun lahir anda : "))

if tahun % 12 == 1:
  print("zodiak cina anda adalah ayam")
elif tahun %12 == 2:
  print("zodiak cina anda adalah anjing")
elif tahun %12 == 3:
  print("zodiak cina anda adalah babi")
elif tahun %12 == 4:
  print("zodiak cina anda adalah tikus")
elif tahun %12 == 5:
  print("zodiak cina anda adalah kerbau")
elif tahun %12 == 6:
  print("zodiak cina anda adalah macan")
elif tahun %12 == 7:
  print("zodiak cina anda adalah kelinci")
elif tahun %12 == 8:
  print("zodiak cina anda adalah naga")
elif tahun %12 == 9:
  print("zodiak cina anda adalah ular")
elif tahun %12 == 10:
  print("zodiak cina anda adalah kuda")
elif tahun %12 == 11:
  print("zodiak cina anda adalah kambing")
elif tahun %12 == 0:
  print("zodiak cina anda adalah monyet")
else:
  print("data yang anda masukkan tidak valid")


