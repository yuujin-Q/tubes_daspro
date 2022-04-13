'''
MODUL F06-Mengubah Stok Game di Toko
Spesifikasi: Mengubah stok game pada toko game dengan memasukkan data
I.S. : input id,dan jumlah game yang ingin ditambahkan
F.S. : game.csv diperbaharui
Desainer dan coder : 16521172, 16521316
'''

# KAMUS LOKAL
# id_game : string
# jumlah, stok_game : int
# file_game : array of array
# 

# ALGORITMA
# IMPORT MODUL
import f16 as save_changes
from f_csvparser import csv_to_arr

# REALISASI FUNGSI
#Fungsi untuk mengubah game pada toko oleh admin
def ubah_game():
    id_game = input("Masukkan ID game: ")
    jumlah = int(input("Masukkan jumlah: "))
    
    # deklarasikan array file game.csv
    file_game = csv_to_arr('game','csv_files')
    
    # ubah stok
    for i in range (len(file_game)):
        if id_game == file_game[i][0]:
            # cari data melalui id game
            stok_game = int(file_game[i][5])
            if jumlah>=0:
                stok_game += jumlah
                print("Stok game " + file_game[i][1] + " berhasil ditambahkan. Stok sekarang: " + str(stok_game))
            else: #jumlah<0
                if stok_game >= (-1)*jumlah:
                    stok_game += jumlah
                    print("Stok game " + file_game[i][1] + " berhasil dikurangi. Stok sekarang: " + str(stok_game))
                else:
                    print("Stok game " + file_game[i][1] + " gagal dikurangi karena stok kurang. Stok sekarang: " + str(stok_game))
            break
        elif i == (len(file_game)-1):
            print("Tidak ada game dengan ID tersebut!")
    #save_changes()
