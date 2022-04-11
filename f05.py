'''
MODUL F05-Mengubah Game pada Toko Game
Spesifikasi: Mengubah game pada toko game dengan memasukkan data
I.S. : input id, nama, kategori, tahun rilis, dan harga game
F.S. : game.csv diperbaharui
Desainer dan coder : 16521172, 16521199
'''

# KAMUS LOKAL
# id_game, nama_game, kategori : string
# tahun_rilis, harga : int

# ALGORITMA
# IMPORT MODUL
import f16 as save_changes
from f_csvparser import csv_to_arr

# REALISASI FUNGSI
#Fungsi untuk mengubah game pada toko oleh admin
def ubah_game():
    id_game = input("Masukkan ID game: ")
    nama_game = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun_rilis = input("Masukkan tahun rilis: ")
    harga = input("Masukkan harga: ")
    
    # deklarasikan array file game.csv
    file_game = csv_to_arr('game','csv_files')
    arr_id = [file_game[i][0] for i in range (len(file_game))]    
    
    # cari id game
    for i in range (len(file_game)):
        if id_game == arr_id[i]:
            if nama_game != '':
                file_game[i][1] = nama_game
            if kategori != '':
                file_game[i][2] = kategori
            if tahun_rilis != '':
                file_game[i][3] = tahun_rilis
            if harga != '':
                file_game[i][4] = harga
            save_changes()
