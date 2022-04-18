'''
MODUL F05-Mengubah Game pada Toko Game
Spesifikasi: Mengubah game pada toko game dengan memasukkan data
I.S. : input id, nama, kategori, tahun rilis, dan harga game
F.S. : game.csv diperbaharui
Desainer dan coder : 16521172, 16521199
'''

# KAMUS LOKAL
    # FUNGSI DAN PROSEDUR
        # common.iterLength(iterable: string or array) -> integer
    # VARIABEL
        # id_game, nama_game, kategori : string
        # tahun_rilis, harga : int
        # arr_id : array of string

# ALGORITMA
# IMPORT MODUL
import f_common as common

# REALISASI FUNGSI
#Fungsi untuk mengubah game pada toko oleh admin
def ubah_game(game):
    # input
    id_game = input("Masukkan ID game: ")
    nama_game = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun_rilis = input("Masukkan tahun rilis: ")
    harga = input("Masukkan harga: ")
    
    # membuat array berisi id game
    arr_id = [game[i][0] for i in range (common.iterLength(game))]    
    
    # cari id game
    for i in range (common.iterLength(game)):
        if id_game == arr_id[i]:
            if nama_game != '':             # jika input nama game tidak kosong
                game[i][1] = nama_game      # maka gantikan elemen nama game dengan input dari pengguna
            if kategori != '':              # jika input kategori game tidak kosong
                game[i][2] = kategori       # maka gantikan elemen kategori game dengan input dari pengguna
            if tahun_rilis != '':           # jika input tahun rilis game tidak kosong
                game[i][3] = tahun_rilis    # maka gantikan elemen tahun rilis game dengan input dari pengguna
            if harga != '':                 # jika input harga game tidak kosong
                game[i][4] = harga          # maka gantikan elemen harga game dengan input dari pengguna
    return game