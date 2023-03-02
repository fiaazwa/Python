data_angka = [3,3,4,4,4,1,2,3,4,5,6,7,8,9,0]
print(f"data angka ={data_angka}")

# count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# ambil posis data
data_huruf = ["ucup","otong","ujang","bambang","asep"]
print(f"data ={data_huruf}")

index_ujang = data_huruf.index["ujang"]
print(f"index ujanga = {index_ujang}")

# mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sort = \n{data_angka}")

print(f"data = \n{data_huruf}")
data_huruf.sort()
print(f"data sort = \n{data_huruf}")

# balik list
data_angka.reverse()
data_huruf.reverse()
print(f"data reverse = \n{data_huruf} \n{data_angka}")




