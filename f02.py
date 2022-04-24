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

def validasiRegis(strings):
    # Spesifikasi : validasi input string yang terbatas alphabet, numerik, underscore, dan strip
    # KAMUS LOKAL
    # nama, username, password : string
    # i : int
    # ALGORITMA
    length = common.iterLength(strings)
    for i in range(length):
        x = ord(strings[i])
        if not ((x >= ord('a') and x <= ord('z')) or (x >= ord('A') and x<= ord('Z')) or (x>=ord('0') and x<=ord('9')) or x == ord('_') or x == ord('-')):
            return False
    return True


# realisasi fungsi
def register (user):
    # input nama, username, dan password
    nama = input("Masukkan nama: ")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    # cek apakah username terpakai
    if nama != '' and username!= '' and password!='' and validasiRegis(username):
        for i in range(common.iterLength(user)):
            if username == user[i][1]:
                # username sudah terpakai
                print("Username " + username + " sudah terpakai, silakan menggunakan username lain.")
                break
            elif i == (common.iterLength(user)-1):
                # username belum terpakai
                print("Username " + username + " telah berhasil register ke dalam " + '"%s"' % "Binomo" + ".")
                user += [[str(common.iterLength(user)),username,nama,password,'User','0']] # menambahkan data user baru ke array user
        
    else:
        print("Masukan tidak valid.")
    return user