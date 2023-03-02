#coutinue , pass, break

#pass -> dia berfungsi dummy, tidak akan dieksekusi
print("pass")
print(10*"="+"\n")
angka = 0

while angka < 5:
    angka += 1

    if angka == 3:
        pass # ini tidak akan di eksekusi
    print(angka)


print("continue")
print(10*"="+"\n")
angka = 0
print (f"angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")

    if angka == 2:
        print("hayoooooo loh..........")
        continue # akan membuat loop kelangkah selanjutnya.

    print("whasssaaaap!")

print("niceee")

print("break")
print(10*"="+"\n")

angka = 0 

while True:
    angka += 1
    print(f"angka sekarang -> {angka}")

    if angka == 2:
        print("hayoooooo loh..........")
        break
    print("whasssaaaap!")

print("cuuukuuup!")











