'''
MODUL F12 - Top Up Saldo 
Spesifikasi: melakukan topup saldo pada User (dilakukan oleh Admin)
I.S. : datauser terdefinisi, username dan saldo diinputkan
F.S. : saldo user pada datauser mengalami perubahan sesuai dengan input
Desainer dan coder : 16521199, 16521316
'''

import f_common as common

#fungsi top up oleh admin
def topup(datauser):
    # SPESIFIKASI {menambahkan atau mengurangi saldo pada seorang user (role User)}
    # KAMUS LOKAL
        # username, saldo : string
        # usernamefound : boolean
        # i, userindex : integer
    # ALGORITMA
    username = input("Masukkan username: ")
    saldo = input("Masukkan saldo: ")

    # pencarian username
    usernamefound = False
    for i in range(1, common.iterLength(datauser)):     # setidaknya ada 1 username (Admin)
        if datauser[i][1] == username:  # jika ketemu, catat indeks, keluar dari pengulangan
            usernamefound = True
            userindex = i
            break
    # penambahan saldo
    if usernamefound and datauser[userindex][4] == 'User':  # jika ketemu username dengan role User
        # validasi input saldo; data saldo terdapat di datauser[userindex][5]
        if int(datauser[userindex][5]) + int(saldo) < 0:    #hasil akhir saldo bernilai negatif
            print("Masukan tidak valid")
        else:
            datauser[userindex][5] = str(int(datauser[userindex][5]) + int(saldo))
            print("Top up berhasil. Saldo " + username + " bertambah menjadi " + datauser[userindex][5])
    else:
        print('Username "'+ username + '" tidak ditemukan.')

    # pengembalian hasil proses
    return datauser