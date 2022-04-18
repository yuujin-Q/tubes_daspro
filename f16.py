'''
MODUL F16-Save
Spesifikasi: Menyimpan semua file setelah dilakukan perubahan pada folder.
I.S. : input nama folder
F.S. : 
Desainer dan coder : 16521172, 16521262
'''

# ALGORITMA
# IMPORT FUNGSI DAN MODUL
import f_common as common
import csv
import os

# REALISASI FUNGSI
def save_file(file,folder,arr):
    # Spesifikasi : Menuliskan array ke csv
    # KAMUS LOKAL
       # filepath : string
       # file_save : SEQFILE of array of string
       # i : integer
    
    filepath = '.\\saves\\' + folder
    filename = file + '.csv'
    
    #for root, dirs, files in os.walk(".\\saves\\", topdown=False):
    #    for name in files:
    #        print(os.path.join(root, name))
    #    for name in dirs:
    #        print(os.path.join(root, name))
    
    with open(filename, 'w') as fp:   # buat file kosong
        pass
    
    file_save = open(os.path.join(filepath,filename), 'w', newline='')
    writer = csv.writer(file_save,delimiter=';')
    
    row = file_save.readline()
    i=0
    while (row):
        writer.writerow(arr[i])
        i+=1
    file_save.close()
    

def update_arr_user (arr, user_arr, user_id):
    # Spesifikasi : memperbaharui array inventory dan history sesuai array userinventory dan userhistory
    # KAMUS LOKAL
    
    for i in range (common.iterLength(user_arr)):   # cek userinventory (game yang dimiliki user)
        for j in range (common.iterLength(arr)):   # cek kepemilikan
            if arr[j][1] == user_id:   # cek data milik user di kepemilikan (berdasarkan user_id)
                if user_arr[i][0] != arr[j][0]:   # jika belum ada game dari userinventory pada kepemilikan
                    arr += user_arr[i]   # tambahkan game "baru" tersebut ke kepemilikan
    return arr

def update_arr_game (game,tokogame):
    # spesifikasi : memperbaharui array game jika ada perbedaan dengan tokogame
    # KAMUS LOKAL
    
    for i in range (common.iterLength(tokogame)):
        for j in range (common.iterLength(game)):
            if (tokogame[i][0]==game[j][0]) and (tokogame[i][5]!=game[j][5]):
                game += [tokogame[i][0],tokogame[i][1],tokogame[i][3],tokogame[i][4],tokogame[i][2],tokogame[i][5]]
    return game


def save(user,game,kepemilikan,riwayat,userinventory,tokogame,userhistory,user_id):
    # Spesifikasi : menyimpan seluruh data ke dalam folder sesuai input pengguna
    # KAMUS LOKAL
    
    folder = input("Masukkan nama folder penyimpanan: ")
    
    arr_string = ['user','game','kepemilikan','riwayat']
    arr_filename = ["user.csv","game.csv","kepemilikan.csv","riwayat.csv"]
    
    update_arr_user(kepemilikan,userinventory,user_id)
    update_arr_user(riwayat,userhistory,user_id)
    update_arr_game (game,tokogame)
    
    if folder not in os.listdir():   # jika folder belum ada
        os.mkdir(folder)    # buat folder baru
        
    for i in range (common.iterLength(arr_filename)):   # menyimpan semua file dalam folder
        save_file(arr_string[i],folder,arr_string[i])   # simpan semua file
    
    print("Saving...")
    print("Data telah disimpan pada folder " + folder + "!")



# uji coba
import f_csvparser as csvparser

kepemilikan = csvparser.csv_to_arr('kepemilikan', 'save0')
game = csvparser.csv_to_arr('game', 'save0')
riwayat = csvparser.csv_to_arr('riwayat', 'save0')
user = csvparser.csv_to_arr('user', 'save0')

userinventory = common.create_inventory_arr(kepemilikan, game, 0) # admin id 0
tokogame = common.create_tokogame_arr(game)
userhistory = common.create_userhistory_arr(riwayat, 0)

save(user,game,kepemilikan,riwayat,userinventory,tokogame,userhistory,0)