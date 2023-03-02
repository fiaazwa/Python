#membuat kalkulato sederhana

print (20*"=")
print("kalkulator sederhana")
print (20*"=" + "\n")

#input angka dan operator
angka1 = float (input("masukkan angka pertama: "))
aritmatika = input("masukkan operator MTK: ")
angka2 = float (input("masukkan angka kedua: "))
hasil = 0

#pengecekan dan hasil
if  aritmatika == "*":
    print(f"hasil dari {angka1} * {angka2} = {hasil}")

elif aritmatika == "/":
    print(f"hasil dari {angka1} / {angka2} = {hasil}")

elif aritmatika == "+":
    print(f"hasil dari {angka1} + {angka2} = {hasil}")

elif aritmatika == "-":
    print(f"hasil dari {angka1} - {angka2} = {hasil}")
