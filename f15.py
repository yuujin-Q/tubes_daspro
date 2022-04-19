'''
MODUL F15-LOAD
Spesifikasi: Admin dapat mendaftarkan pengguna baru
I.S. : Program belum dijalankan
F.S. : Data di-load
Desainer dan coder : 16521172, 16521199
'''

# KAMUS LOKAL
    # FUNGSI DAN PROSEDUR
        # csv_to_arr (input filename, folder : string, output arr : array of array of string)
    # VARIABEL
        # user, game, riwayat, kepemilikan : array of array of string
    
# ALGORITMA
# IMPORT MODUL DAN FUNGSI
from f_csvparser import csv_to_arr

# REALISASI FUNGSI
def load (nama_folder):
    print("Loading...")   # mencetak ke layar
    # menuliskan data pada file csv ke dalam bentuk array of array of string
    user = csv_to_arr('user',nama_folder)
    game = csv_to_arr('game',nama_folder)
    riwayat = csv_to_arr('riwayat',nama_folder)
    kepemilikan = csv_to_arr('kepemilikan',nama_folder)
    # output (cetak ke layar)
    print("Selamat datang di antarmuka", '"%s"' % "Binomo")
    return user,game,riwayat,kepemilikan   # mengembalikan array