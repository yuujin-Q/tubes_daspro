'''
MODUL F16-Save
Spesifikasi: Menyimpan semua file setelah dilakukan perubahan pada folder.
I.S. : input nama folder
F.S. : file user.csv, game.csv, kepemilikan.csv, dan riwayat.csv dibuat pada folder sesuai input
Desainer dan coder : 16521172, 16521262, 16521316
'''

# ALGORITMA
# IMPORT FUNGSI DAN MODUL
import f_common as common
import os

# REALISASI FUNGSI
def writecsv (arr,folder,filename):
    # Spesifikasi : Menuliskan array of array of string ke dalam file csv
    # KAMUS LOKAL
        # path, str : string
        # csvdat : SEQFILE of string
    # ALGORITMA
    filename += '.csv'   # menambahkan format file .csv pada nama file
    path = os.path.join(folder,filename)   # menuliskan path file
    str = common.arrarr_to_str(arr,';')   # mengubah array menjadi string dengan delimiter ';'
    csvdat = open(path,'w')   # membuka file csv
    csvdat.write(str)   # menuliskan array yang sudah diubah menjadi string ke dalam csv
    csvdat.close()   # menutup file csv
    
def save (user,game,riwayat,kepemilikan):
    # Spesifikasi : Menyimpan data user, game, kepemilikan, dan riwayat ke folder yang diinginkan
    # KAMUS LOKAL
        # folder, path : string
    # ALGORITMA
    # meminta input nama folder tempat semua file csv akan disimpan
    folder = input("Masukkan nama folder penyimpanan: ")
    
    if folder not in os.listdir('.\\saves'):   # jika folder belum ada
        os.mkdir('.\\saves\\'+folder)    # maka buat folder baru
    path = os.path.join('.\\saves\\',folder)   # buat path folder
    
    # menuliskan array ke dalam file csv
    writecsv(user,path,'user')
    writecsv(game,path,'game')
    writecsv(kepemilikan,path,'kepemilikan')
    writecsv(riwayat,path,'riwayat')
    
    # output
    print("Saving...")
    print("Data telah disimpan pada folder " + folder + "!")