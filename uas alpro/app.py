# tugas 1
kata = ("kamu ganteng sekali")
print(kata[::-1])
kata = ("Masa sih")
print(kata[::-1])
kata = ("Hari ini kita ujian ya")
print(kata[::-1])

print("\n")

# tugas 2
count = 1
for i in range(5):
    print(" * "*count)
    count +=1
for i in range(6):
    print(" * "*count)
    count -=1
print("\n")

# tugas 3

while True:
    print("="*20,"menu kami","="*20)
    menu = {
        "1.BU":"Bakso Urat - Rp15000",
        "2.NG":"Nasi Goreng - Rp10000",
        "3.ET":"Es Teh - Rp5000",
        "4.AK":"Ayam Krispi - Rp10000"
    }
    for items in menu.items():
        print(items)

    while True:
        pilihan = int(input("pilih menu dan 'q' untuk menyelesaikan: "))
        jumlah = int(input("jumlah: "))

        if pilihan == 1:
            harga = (jumlah*15000)
            print(jumlah,"Bakso Urat = Rp" ,harga)
            namamenu = ("Bakso Urat")
            print("pesanan anda telah di antar")
        elif pilihan == 2:
            harga = (jumlah*10000)
            print(jumlah,"Nasi Goreng = Rp",harga)
            namamenu = ("Nasi Goreng")
            print("pesanan anda telah di antar")
        elif pilihan == 3:
            harga = (jumlah*5000)
            print(jumlah,"Es TEh = Rp",harga)
            namamenu = ("Es Teh")
            print("pesanan anda telah di antar")
        elif pilihan == 4:
            harga = (jumlah*10000)
            print(jumlah,"Ayam Krispi",harga)
            namamenu = ("Ayam Krispi")
            print("pesanan anda telah di antar")
        else:
            print("maaf yang anda pilih tidak ada pada menu")

        total = harga

        print("\nTotal harus Dibayar: Rp",total)
        bayar=int(input("Uang Tunai Pembeli: Rp "))
        kurang =int(total - bayar)
        kembalian=int(bayar-total)

        if bayar > total:
            print(f'jumlah kembalian anda adalah {kembalian}')
        elif bayar == total:
            print('uang anda pas, terimakasih telah berbelanja ')
        else:
            print(f'maaf uang anda tidak cukup, uang anda kurang {kurang}')

        pesan_lagi = input(f"ingin pesan lagi? (y/n)")
        if pesan_lagi == 'n':
            print("Terimakasih telah bebelanja")
            break





