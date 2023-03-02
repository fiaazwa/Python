# # #latihan perulangan membuat segitiga

# sisi = 6
# #dumay variabel
# print("awal dari for")
# count = 1
# for i in range(4):
#     print(" * "*count)
#     count +=1
# print("akhir dari for\n")

# #mengguanakan while
# print("awal while")
# count=1
# while True:
#     print("*"*count)
#     count +=1

#     if count > sisi:
#         break


# # hanya ganjil saja
# print("awal dari for")
# count = 1
# for i in range(4):
#     print("*"*count)
#     count +=1
# print("akhir dari for\n")

# #mengguanakan while
# print("awal while")
sisi = 6
count=1
spasi = int(sisi/2)
print("spasi")
while True:
    if (count %2):
        #akan print jika ganjil
        print(" "*spasi,"*"*count)
        spasi -=1
        count +=1
    else:
        # akan kembali ke atas jika ganjil
        count +=1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break



a = 5
print("persegi")
for i in range(a):
    print(" * "*a)
print("\n")

print("persegi panjang")
for i in range(a):
    print(" * "*8)
print("\n")

print("sgitiga kiri datar")
count = 1
for i in range(5):
    print(" * "*count)
    count +=1
print("\n")

print("segitiga kanan datar")
b = 1
c = 1
d =int(b / c)
for i in range(5):
    print(" * "*b)
    b += 1






