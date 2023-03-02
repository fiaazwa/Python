# Program 1
sisi_a = int(input("masukkan sisi a : "))
sisi_b = int(input("masukkan sisi b : "))
sisi_c = int(input("masukkan sisi c : "))

if sisi_a == sisi_b and sisi_c == sisi_a and sisi_c:
    print("segitiga tersebut adalah segitiga sama sisi") 
if sisi_a == sisi_b or sisi_b == sisi_c or sisi_c == sisi_a:
    print("segitiga tersebut adalah segitiga sama kaki")
else:
    print("segitiga tersebut adalah segitiga sembaranga")


# # Program 2
# # Menentukan tahun kabisat input user
# tahun = int(input("masukkan tahun kabisat : "))
# # Menentukan tahun kabisat
# if tahun % 40 == 0:
#     print("adalah tahun kabisat")
# if tahun % 100 == 0:
#     print("bukan tahun kabisat")
# if tahun % 4 == 0:
#     print("adalah tahun kabisat")
# else:
#     print("bukan tahun kabisat")


# Program 3
# menentukan zodiak yunani 
tanggal_lahir = int(input("masukkan tanggal lahir anda : "))
bulan_lahir = int(input("masukkan bulan lahir anda : "))

if (tanggal_lahir >= 21 and bulan_lahir == 3) or (tanggal_lahir <= 19 and bulan_lahir == 4):
    print("zodiak anda adalah aries")
elif (tanggal_lahir >= 20 and bulan_lahir == 4) or (tanggal_lahir <= 20 and bulan_lahir == 5):
    print("zodiak anda adalah taurus")
elif (tanggal_lahir >= 21 and bulan_lahir == 5) or (tanggal_lahir <= 20 and bulan_lahir == 6):
    print("zodiak anda adalah gemini")
elif (tanggal_lahir >= 21 and bulan_lahir == 6) or (tanggal_lahir <= 22 and bulan_lahir == 7):
    print("zodiak anda adalah cancer")
elif (tanggal_lahir >= 23 and bulan_lahir == 7) or (tanggal_lahir <= 22 and bulan_lahir == 8):
    print("zodiak anda adalah leo")
elif (tanggal_lahir >= 23 and bulan_lahir == 8) or (tanggal_lahir <= 22 and bulan_lahir == 9):
    print("zodiak anda adalah virgo")
elif (tanggal_lahir >= 23 and bulan_lahir == 9) or (tanggal_lahir <= 22 and bulan_lahir == 10):
    print("zodiak anda adalah libra")
elif (tanggal_lahir >= 23 and bulan_lahir == 10) or (tanggal_lahir <= 21 and bulan_lahir == 11):
    print("zosiak anda adalah scorpio")
elif (tanggal_lahir >= 22 and bulan_lahir == 11) or (tanggal_lahir <= 21 and bulan_lahir == 12):
    print("zodiak anda adalah sagitarius")
elif (tanggal_lahir >= 22 and bulan_lahir == 12) or (tanggal_lahir <= 19 and bulan_lahir == 1):
    print("zodiak anda adalah capricorn")
elif (tanggal_lahir >= 20 and bulan_lahir == 1) or (tanggal_lahir <= 18 and bulan_lahir == 2):
    print("zodiak anda adalah aquarius")
elif (tanggal_lahir >= 19 and bulan_lahir == 2) or (tanggal_lahir <= 20 and bulan_lahir == 3):
    print("zodiak anda adalah pisces")
else:
    print("data yang di masukkan tidak valid")