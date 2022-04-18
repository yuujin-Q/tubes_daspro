'''
MODUL F15-LOAD
Spesifikasi: Admin dapat mendaftarkan pengguna baru
I.S. : Program belum dijalankan
F.S. : Data di-load
Desainer dan coder : 16521172, 16521199
'''

# KAMUS LOKAL
    # FUNGSI DAN PROSEDUR
        #
    # VARIABEL
        # path : string
        # isFolderExist : boolean
        # user, game, riwayat, inventory : array of array of string
    
# ALGORITMA

import f_common as common
from f_csvparser import csv_to_arr
import os
import argparse

def load (nama_folder):
    # cek apakah nama_folder ada atau tidak
    path = '.\\saves\\' + nama_folder # path folder
    isFolderExist = os.path.exists(path) # cek apakah folder ada
    
    # output
    if nama_folder==None: # jika tidak ada parameter
        print("Tidak ada nama folder yang diberikan!")
        print("Usage: python program_binomo.py <nama_folder>")
    else:
        if not isFolderExist:
            print("Folder",'"%s"' % nama_folder,"tidak ditemukan.")
        else:
            print("Loading...")
            user = csv_to_arr('user',nama_folder)
            game = csv_to_arr('game',nama_folder)
            riwayat = csv_to_arr('riwayat',nama_folder)
            inventory = csv_to_arr('kepemilikan',nama_folder)
            print("Selamat datang di antarmuka", '"%s"' % "Binomo")

#load ('save0')