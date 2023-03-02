# materi list
print("mengenal/materi list")
print(20*"="+"\n")

# kumpulan data nomor
data_angka = [1,2,3,4]
print(data_angka)

# kumpulan data string
data_str = ["ucup","otong","bambang"]
print(data_str)

# kumpulan bool
data_bool = [False,True,True,True]
print(data_bool)

# kumpulan campuran
data_campuran = [False,True,2,4,5,67,True,True,"lalang","mahiko"]
print(data_campuran)

## cara alternatif membuat list
data_range = range(1,10)
print(data_range)
data_list = list(data_range)
print(data_list)

## membuat list dengan for
x = int(input("masukkan angka: "))
y = int(input("masukkan angka: "))
y += 3
list_for =[i*i for i in range(x,y)]
print(list_for)

# membuat list dgn for dan if
y += 1
list_for_if = [i for i in range(x,y) if i != 5]
print(list_for_if)

# membuat list dgn for dan if angka genap
list_for_if = [i for i in range(0,10) if i %2 == 0]
print(list_for_if)

# membuat list dgn for dan if angka ganji
list_for_if = [i for i in range(0,10) if i %2 != 0]
print(list_for_if)
print(20*"="+"\n")





print("manipulasi list")
print(15*"="+"\n")

# index  0(-3)  1(-2)   2(-1)
data = ["ucup","otong","bambang"]

# mengambil data ini
data_0 = data[0]
print(f"data pertama(index_0) = {data_0}")

data_akhir = data [-1]
print(f"data terakhir adalah = {data_akhir}")

data_ucup = data [-3]
print(f"data ucup = {data_ucup}")

# melihat info jumlah data pada list
panjang_data = len(data)
print(f"panjang data adalah = {panjang_data}")

## amnipulasi data list

# menambah item pada list
print(f"data sebelum ditambah = \n {data}")

#data.insert(posisi,item)
data.insert(2,"markonah")
print(f"data sesudah ditambah = \n {data}")

# menambah diakhir list
data.append("ujang")
print(f"data ditambah lagi \n {data}")

# menambahkan list dengan list
data_baru = ["asep","mario","shuya"]
data.extend(data_baru)
print(f"data gabungan = \n {data}")

# merubah data/ mengubah data 2 
data[2] = "kurama"
print(f"data ubah = \n {data}")

# menghapus/delete data
data.remove("asep")
print(f"menghapus data = \n {data}")

# menghapus data paling belakang
data_akhir=data.pop()
print(f"menghapus data akhir = \n {data}")
print(data_akhir)



