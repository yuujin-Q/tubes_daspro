'''
MODUL F06-Mengubah Stok Game di Toko
Spesifikasi: Mengubah stok game pada toko game dengan memasukkan data
I.S. : input id,dan jumlah game yang ingin ditambahkan
F.S. : game.csv diperbaharui
Desainer dan coder : 16521172, 16521316
'''

# KAMUS LOKAL
# id_game : string
# jumlah: int
# file_game : array of array

# ALGORITMA
# IMPORT MODUL
import csv
import f_common as common
from f_csvparser import csv_to_arr

# REALISASI FUNGSI
#Fungsi untuk mengubah game pada toko oleh admin
def ubah_game():
    global game    

    id_game = input("Masukkan ID game: ")

    # ubah stok
    for i in range (common.iterLength(game)):
        if id_game == game[i][0]:
            jumlah = int(input("Masukkan jumlah: "))

            # cari data melalui id game
            
            if jumlah>=0:
                game[i][5] = str(int(game[i][5]) + jumlah)
                print("Stok game " + game[i][1] + " berhasil ditambahkan. Stok sekarang: " + game[i][5])
            else: #jumlah<0
                if int(game[i][5]) >= (-1)*jumlah:
                    game[i][5] = str(int(game[i][5]) + jumlah)
                    print("Stok game " + game[i][1] + " berhasil dikurangi. Stok sekarang: " + game[i][5])
                else:
                    print("Stok game " + game[i][1] + " gagal dikurangi karena stok kurang. Stok sekarang: " + game[i][5])
            break
        elif i == (common.iterLength(game)-1):
            print("Tidak ada game dengan ID tersebut!")




# UJI COBA
# game = csv_to_arr('game', 'save0')

# for i in range(common.iterLength(game)):
#     print(game[i])

# print()

# ubah_game()

# print()
# for i in range(common.iterLength(game)):
#     print(game[i])
