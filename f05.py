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

# REALISASI FUNGSI
#Fungsi untuk mengubah game pada toko oleh admin
def ubah_game():
    id_game = input("Masukkan ID game: ")
    nama_game = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun_rilis = input("Masukkan tahun rilis: ")
    harga = input("Masukkan harga: ")
    
    # akses file game.csv
    #folder = 'admin'
    #path = folder + '\game.csv'
    #file = open(path,'r')
    #lines = file.readlines()
    
    # cari id game
    
        
    save_changes