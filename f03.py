'''
MODUL F03-LOGIN
Spesifikasi: User dapat login dengan memasukkan username dan password.
I.S. : input username, password
F.S. : 

Desainer dan coder : 16521262
'''

import f_common as common

def login(datauser):
    # SPESIFIKASI: memeriksa username dan password user
    # KAMUS LOKAL
        # i : integer
        # common.iterLength(iterable : string or array) -> integer
    
    # ALGORITMA
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # mencari data user
    found = False
    for i in range(1, common.iterLength(datauser)):
        # apabila username ditemukan dan sesuai dengan passwordnya
        if username == datauser[i][1] and password == datauser[i][3]:
            print("Halo " + datauser[i][2] + "! Selamat datang di " + '"%s"' % "Binomo" + ".")
            found = True
            user_id = int(datauser[i][0])
        
        
    if not found:
        if username =='' or password =='':  # apabila ada input kosong
            print("Anda belum memasukkan username dan/atau password!")
        else:   # apabila username tidak ditemukan atau username & password tidak cocok
            print('Password atau username salah atau tidak ditemukan.')
        user_id = -1


    
    return found,user_id