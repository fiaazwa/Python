# latihan list
# membuat databes sederhana_list buku

list_buku =[]
while True:
    print("\nmasukkan data buku")
    judul = input(" judul buku\t")
    penulis = input("nama penulis\t")
    penerbit = input("penerbit\t")

    buku_baru = [judul,penulis,penerbit]
    list_buku.append(buku_baru)

    print("\n")
    for index,buku in enumerate (list_buku):
        print(f"{index+1}| {buku[0]}| {buku[1]}")

    print("\n")
    islanjut = input("apakah dilanjutkan? (y/n)")

    if islanjut == "n":
        break

print("PROGRAM SELESAI")


