## teknik duplikat list

a = ["ucup","otong","ujang","bambang","asep"]
print(f"a = {a}")

b = a
print(F"b = {b}\n")# pass by refrence

# memngubah member a

a[0] = "mikkey"
b.sort()
print(f"a = {a}")
print(f"b = {b}\n")

# addres dari list a dan b
print(f"addres a = {hex(id(a))}")
print(f"addres b = {hex(id(b))}\n")

# duplikat list dengan copy
c = a.copy()# full dublikat

print(f"addres a = {hex(id(a))}")
print(f"addres a = {hex(id(a))}")
print(f"addres c = {hex(id(c))}\n")

c[0] = "ika"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}\n")


