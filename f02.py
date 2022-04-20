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
        # common.iterLength(iterable: string or array) -> integer
    # VARIABEL
        # nama, username, password : string
        # i : int
        
# ALGORITMA
# import modul yang diperlukan
import f_common as common

# realisasi fungsi
def register (user):
    # input nama, username, dan password
    nama = input("Masukkan nama: ")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    # cek apakah username terpakai
    for i in range(common.iterLength(user)):
        if username == user[i][1]:
            # username sudah terpakai
            print("Username " + username + " sudah terpakai, silakan menggunakan username lain.")
            break
        elif i == (common.iterLength(user)-1):
            # username belum terpakai
            print("Username " + username + " telah berhasil register ke dalam " + '"%s"' % "Binomo" + ".")
            user += [[str(common.iterLength(user)-1),username,nama,password,'user','0']] # menambahkan data user baru ke array user
    return user