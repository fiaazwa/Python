# # list didalam list
# data_0 = [1,2,3]
# data_1 = [3,4,5,6]

# list_2d = [data_0,data_1,6,7]
# print(f"list_2d = {list_2d}")

# # contah penggunaan

# peserta_0 = ["ucup",25,"cwo"]
# peserta_1 = ["ujang",10,"cwo"]
# peserta_2 = ["mahik",22,"cwo"]

# list_peserta =[peserta_0,peserta_1,peserta_2]
# print(f"peserta ={list_peserta}")

# for peserta in list_peserta:
#     print(f"nama\t: {peserta[0]}")
#     print(f"umur\t: {peserta[1]}")
#     print(f"gender\t: {peserta[2]}\n")

# # dengan reference

# list_copy = list_peserta.copy()
# print(f"peserta ={list_copy}\n")
# peserta_0[0] = "michale"
# print(f"peserta ={list_copy}")
# print(f"peserta ={list_peserta}")

## deep copy nested list
print(f"Deep Copy Nested List")
print(21*"="+"\n")

data_0 = [1,2]
data_1 = [3,4]
 
data_2D = [data_0,data_1,10]
data_2D_copy = data_2D.copy()

print(f"list_2d = {data_2D}")
print(f"data copy = {data_2D_copy}")

# mengambil data dari nested list

data = data_2D[1][0]
print(f"data = {data}")
 
# address semuanya

print(f"address asli ={hex(id(data_2D))}")
print(f"address copy ={hex(id(data_2D_copy))}")

print("address dari member ke-1")

print(f"address asli ={hex(id(data_2D[0]))}")
print(f"address copy ={hex(id(data_2D_copy[0]))}")


data_2D[1][0] = 5
data_2D[2] = 9
print(f"list_2d = {data_2D}")
print(f"data copy = {data_2D_copy}")

# deepcopy
from copy import deepcopy

data_2D = [data_0,data_1,10]
data_2D_deepcopy = deepcopy(data_2D)

print(f"address asli ={hex(id(data_2D))}")
print(f"address deep ={hex(id(data_2D_deepcopy))}")

print("address dari member ke-1")

print(f"address asli ={hex(id(data_2D[0]))}")
print(f"address deep ={hex(id(data_2D_deepcopy[0]))}")


data_2D[1][0] = 30
print(f"data = {data_2D}")
print(f"data asli ={data_2D_copy}")
print(f"data deep ={data_2D_deepcopy}")


