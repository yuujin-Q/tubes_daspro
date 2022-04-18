'''
MODUL F11-Mencari Game di Toko dari ID, Nama Game, Harga, Kategori dan Tahun Rilis 
Spesifikasi: Mencari Game di Toko dari ID, Nama Game, Harga, Kategori dan Tahun Rilis 
I.S. : toko terdefinisi, input id, nama game, harga, kategori, tahun rilis yang ingin digunakan dalam pencarian
F.S. : output data game hasil pencarian berdasarkan input
Desainer dan coder : 16521199, 16521316
'''

import f_common as common

#prosedur untuk mencari game di toko oleh user dan admin
def search_game_at_store(toko):
    #SPESIFIKASI {Melakukan pencarian game di toko oleh user dan admin}
    #KAMUS LOKAL
        # id_game, nama_game, kategori, harga, tahun_rilis : string
        # id_kosong, nama_kosong, harga_kosong, kat_kosong, tahun_kosong : boolean
        # count, i : integer
        # search_result : array of array of string
    #ALGORITMA
    id_game = input("Masukkan ID game: ")
    nama_game = input("Masukkan Nama game: ")
    harga = input("Masukkan Harga Game: ")
    kategori = input("Masukkan Kategori Game: ")
    tahun_rilis = input("Masukkan Tahun Rilis Game: ")
    print()
    print("Daftar game pada toko yang memenuhi kriteria: ")

    # jika ada input yang kosong, assign boolean True (digunakan dalam logika pencarian)
    if id_game == '': id_kosong = True
    else: id_kosong = False
    if nama_game == '': nama_kosong = True
    else: nama_kosong= False
    if harga == '': harga_kosong = True
    else: harga_kosong = False
    if kategori == '': kat_kosong = True
    else: kat_kosong= False
    if tahun_rilis == '': tahun_kosong = True
    else: tahun_kosong = False

    # search
    count = 0
    search_result = []
    for i in range(common.iterLength(toko)):
        if (
            (id_game == toko[i][0] or id_kosong) and (nama_game == toko[i][1] or nama_kosong) and (harga == toko[i][2] or harga_kosong) 
            and (kategori == toko[i][3] or kat_kosong) and (tahun_rilis == toko[i][4] or tahun_kosong)
        ):
            count +=1
            search_result += [toko[i]]
    
    # output
    if count == 0: # tidak ada game
        print("Tidak ada game pada toko yang memenuhi kriteria")
    else:       # minimal ada satu game
        search_result = common.alignTable(search_result)        # menyejajarkan posisi string dalam array
        for i in range(common.iterLength(search_result)):
            print(f'{i+1}. ' + common.arr_to_str(search_result[i],' | ')) # output dalam bentuk tabel yang sudah rapi

