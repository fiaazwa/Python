# # list
# data_list = [1,2,3,4,5] # menggunakan kurung siku
# print(data_list)

# # tuples
# data_tuples = (1,2,3,4,5)
# print(data_tuples)

# import calendar

# yy = 2023
# mm = 3

# # memuat calendar
# print(calendar.month(yy,mm))

import os

shutdown = input("shutdown your PC? (yes/no):") 

if shutdown == "no":
    exit()
else:
    os.system("shutdown /s /t 1")