'''
MODUL F02-REGISTER
Spesifikasi: Admin dapat mendaftarkan pengguna baru
I.S. : input nama, username, password
F.S. : pengguna terdaftar sebagai user (jika username belum pernah terpakai)
atau tidak terdaftar sebagai user (jika username sudah terpakai)
Desainer dan coder : 16521172
'''

# KAMUS LOKAL
    # FUNGSI DAN PROSEDUR
        # csv_to_arr(filename,folder: string) -> array of string
        # common.iterLength(iterable: string or array) -> integer
    # VARIABEL
        # nama, username, password : string
        # user : array of array of string
        # data_username : array of string
        
# ALGORITMA
# import modul yang diperlukan
from f_csvparser import csv_to_arr
import f_common as common

# realisasi fungsi
def register ():
    # input nama, username, dan password
    nama = input("Masukkan nama: ")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    # deklarasikan array file user.csv
    user = csv_to_arr('user','save0')
    data_username = [user[i][1] for i in range (1,common.iterLength(user))]
    
    # cek apakah username terpakai
    for i in range(common.iterLength(data_username)):
        if username == data_username[i]:
            # username sudah terpakai
            print("Username " + username + " sudah terpakai, silakan menggunakan username lain.")
        elif i == (common.iterLength(data_username)-1):
            # username belum terpakai
            print("Username " + username + " telah berhasil register ke dalam " + '"%s"' % "Binomo" + ".")
            user += [[str(common.iterLength(user)-1),username,nama,password,'user','0']] # menambahkan data user baru ke array user
    return user