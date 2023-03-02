# looping list

# for loop
kumpulan_angka = [1,2,3,4,5]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta =["ucup","diding","dudung","ucok"]
for nama in peserta:
    print(f"nama = {nama}")

# for loop dan range
print('\n for loop dan range')
kumpulan_angka=[3,5,3,10,9,8]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")


# while
print("\n while loop")
kumpulan_angka=[3,5,3,10,9,8]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

# list comprehension
print("list Comprehension")
data = ["ucup",2,3,4,"bambang"]

[print (i) for i in data]

angka = [10,2,7,8,9,12]

angka_kuadrad = [i**2 for i in angka]
print(angka_kuadrad)
# enumerate
print("\nenumerate")
data_list = ["ucup",3,4,5,"bambang"]

for index,data in enumerate(data_list):
    print(f"index = {index}, data = {data}")

