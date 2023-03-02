#membuat game suit
import random
print ("===game suit===")
player = input("masukkan [batu, gunting ,kertas]: ").lower()
#komputer
komputer = ""
rand = random.randrange(0,11)
if rand >= 0 and rand <=3:
    komputer = "gunting"
    #tentukan rute
    if "kertas" in player: hasil = "kamu kalah"    
    elif "batu" in player: hasil = "kamu menang"
    else: hasil = "kita seri"    

elif rand >3 and rand <=6:
    komputer = "kertas"
    #tentukan rute
    if "batu" in player: hasil = "kamu kalah"    
    elif "gunting" in player: hasil = "kamu menang"
    else: hasil = "kita seri"    

else:
    komputer = "batu"
    #tentukan rute
    if "kertas" in player: hasil = "kamu menang"    
    elif "gunting" in player: hasil = "kamu kalah"
    else: hasil = "kita seri"    

print("saya {komputer} kamu {player} hasil {hasil}")