'''
MODUL F02-REGISTER
Spesifikasi: Admin dapat mendaftarkan pengguna baru
I.S. : input nama, username, password
F.S. : pengguna terdaftar sebagai user (jika username belum pernah terpakai)
atau tidak terdaftar sebagai user (jika username sudah terpakai)
Desainer dan coder : 16521172
'''

# KAMUS LOKAL
# nama, username, password : string
# file_user : file csv
# folder, path : string
# lines : function readlines
# count_line, index_line : int

# ALGORITMA
# import modul yang diperlukan
from f16 import save_changes
from f_csvparser import csv_to_arr

# realisasi fungsi
def register ():
    # input nama, username, dan password
    nama = input("Masukkan nama: ")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    # deklarasikan array file user.csv
    file_user = csv_to_arr('user','csv_files')
    data_username = [file_user[i][1] for i in range (len(file_user))]
    
    # cek apakah username terpakai
    found = False
    i=0
    while (found == False) and (i<(len(file_user))):
        if username == data_username[i]:
            # username sudah terpakai
            print("Username " + username + " sudah terpakai, silakan menggunakan username lain.")
            found = True
        elif i == (len(file_user) - 1):
            # username belum terpakai
            print("Username " + username + " telah berhasil register ke dalam " + '"%s"' % "Binomo" + ".")
            save_changes()
        i += 1
