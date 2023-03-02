#logika boolean 
#AND,OR,NOT,XOR


print("------topik and------")
a = False
b = False
c = a and b
print("data c=",c)

a = False
b = True
c = a and b 
print("data c=",c)

a = True
b = False
c = a and b
print("data c=",c)

a = True
b = True
c = a and b
print("data c=",c)


print("------topik or-----")

P = False
Q = False
R = P or Q
print("data R=",R)

P = False
Q = True
R = P or Q
print("data R=",R)

P = True
Q = False
R = P or Q
print("data R=",R)

P = True 
Q = True
R = P or Q
print("data R=",R)

print("-----topik not-----")


x = False
y = not x
print("data y=",y)

x = True
y = not x
print("data y=",y)

print("------topik xor ------")

m = False
n = False
o = m ^ n
print("data o=",o)

m = False
n = True
o = m ^ n
print("data o=",o)

m = True
n = False
o = m ^ n
print("data o=",o)

m = True
n = True
o = m ^ n
print("data o=",o)




