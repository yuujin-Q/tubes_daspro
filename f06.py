'''
MODUL F06-Mengubah Stok Game di Toko
Spesifikasi: Mengubah stok game pada toko game dengan memasukkan data
I.S. : input id,dan jumlah game yang ingin ditambahkan
F.S. : game.csv diperbaharui
Desainer dan coder : 16521172, 16521316
'''

# KAMUS LOKAL
    # FUNGSI DAN PROSEDUR
        # common.iterLength(iterable: string or array) -> integer
    # VARIABEL
        # id_game : string
        # i, jumlah: integer


# ALGORITMA
# IMPORT MODUL
import f_common as common

# REALISASI FUNGSI
#Fungsi untuk mengubah game pada toko oleh admin
def ubah_game():
    global game    # variabel global

    id_game = input("Masukkan ID game: ") # input dari pengguna

    # ubah stok
    for i in range (common.iterLength(game)):
        if id_game == game[i][0]:       # jika id game ditemukan, maka minta input jumlah perubahan stok
            jumlah = int(input("Masukkan jumlah: "))

            # cari data melalui id game
            if jumlah>=0: # penambahan stok
                game[i][5] = str(int(game[i][5]) + jumlah)
                print("Stok game " + game[i][1] + " berhasil ditambahkan. Stok sekarang: " + game[i][5])
            else:         # pengurangan stok
                if int(game[i][5]) >= (-1)*jumlah:      # hasil pengurangan valid (tidak negatif)
                    game[i][5] = str(int(game[i][5]) + jumlah)
                    print("Stok game " + game[i][1] + " berhasil dikurangi. Stok sekarang: " + game[i][5])
                else:                                   # hasil pengurangan tidak valid (negatif)
                    print("Stok game " + game[i][1] + " gagal dikurangi karena stok kurang. Stok sekarang: " + game[i][5])
            break
        elif i == (common.iterLength(game)-1):      # jika id game tidak ditemukan
            print("Tidak ada game dengan ID tersebut!")

