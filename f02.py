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
import f16 as save_changes

# realisasi fungsi
def register ():
    # input nama, username, dan password
    nama = input("Masukkan nama: ")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # panggil modul parser
    ## cek apakah username unik
    ## membuka file user.csv dari folder
    #folder = 'admin'
    #path = folder + '\user.csv'
    #file_user = open(path, 'r')
    #lines = file_user.readlines()
    #count_line = 0
    #
    ## menghitung jumlah baris dalam file user.csv
    #for user in lines:
    #    count_line += 1
    #
    ## mencari username pada file user.csv
    #if count_line>0:
    #    # jika ada data user, maka cek
    #    index_line = 0
    #    for user in lines:
    #        index_line += 1
    #        if (username == user):
    #            # jika username sudah terpakai
    #            print("Username " + username + " sudah terpakai, silakan menggunakan username lain.")
    #        elif (count_line == index_line):
    #            # jika username belum pernah terpakai (sudah cek sampai baris terakhir)
    #            print("Username " + username + " telah berhasil register ke dalam " + '"%s"' % "Binomo" + ".")
    #            save_changes
    #else:
    #    # jika belum ada data user, maka dapat langsung terdaftar
    #    print("Username " + username + " telah berhasil register ke dalam " + '"%s"' % "Binomo" + ".")
    #    save_changes