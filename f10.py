'''
MODUL F10-Mencari Game yang Dimiliki dari ID dan Tahun Rilis
Spesifikasi: Mencari game yang dimiliki dari ID dan tahun rilis
I.S. : input id dan tahun rilis game yang ingin dicari
F.S. : output data game tersebut
Desainer dan coder : 16521172, 16521316
'''

# KAMUS LOKAL
# id_game : string
# tahun_rilis : int
# inventory, games : array of array
# count_search : int
# id, tahun: boolean

# ALGORITMA
from itertools import count
import f_common as common

# REALISASI FUNGSI
def search_my_game(inventory, games, userid):
    id_game = input("Masukkan ID Game: ")
    tahun_rilis = input("Masukkan Tahun Rilis Game: ")
    print()
    print("Daftar game pada inventory-mu yang memenuhi kriteria:")
    
    if id_game == '':       # jika id_game kosong
        id = True
    else:
        id = False
    if tahun_rilis == '':   # jika tahun_rilis kosong
        tahun = True
    else:
        tahun = False

    # search

    
    # count_search = 0
    # for j in range(1, common.iterLength(games)):   #pemrosesan traversal per baris
    #     # cari game berdasarkan tahun rilis di game.csv
    #     if (id_game == games[j][0] and tahun) or (tahun_rilis == games[j][3] and id) or (id_game == games[j][0] and tahun_rilis== games[j][3]):
    #         for i in range (common.iterLength(inventory)):
    #             # cari game di kepemilikan.csv
    #             if inventory[i][0] == games[j][0] and inventory[i][1] == userid: #cari id
    #                 print(games[j][0] + " | " + games[j][1] + " | " + games[j][4] + " | " + games[j][5] + " | " + str(tahun_rilis))
    #                 count_search+=1
    #             # elif id and tahun_rilis == games[j][3]:
    # if (id and tahun):
    #     for i in range (common.iterLength(inventory)):
    #         if inventory[i][1] == userid:
    #             for j in range(1,common.iterLength(games)):
    #                 if inventory[i][0] == games[j][0]:
    #                     print(games[j][0] + " | " + games[j][1] + " | " + games[j][4] + " | " + games[j][5] + " | " + str(tahun_rilis))
    #                     count_search+=1

                
    # if count_search==0:
    #     print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
    
    if id_game=="":
        for j in range(common.iterLength(games)):
            # cari game berdasarkan tahun rilis di game.csv
            if j>0 and tahun_rilis == int(games[j][3]): #kalau sama
                for i in range (common.iterLength(inventory)):
                    # cari game di kepemilikan.csv
                    if inventory[i][0] == games[j][0]:
                        print(games[j][0] + " | " + games[j][1] + " | " + games[j][4] + " | " + games[j][5] + " | " + str(tahun_rilis))
                        count_search+=1
        if count_search==0:
            print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
    else:
        for i in range (common.iterLength(inventory)):
            if id_game == inventory[i][0]:
                for j in range (common.iterLength(games)):
                    if id_game == games[j][0] and tahun_rilis == int(games[j][3]):
                        print(games[j][0] + " | " + games[j][1] + " | " + games[j][4] + " | " + games[j][5] + " | " + str(tahun_rilis))
                        count_search+=1
        
            elif i==(common.iterLength(inventory)-1) and count_search==0: #tidak ada game yang cocok
                print("Tidak ada game pada inventory-mu yang memenuhi kriteria")

# UJI COBA
from f_csvparser import csv_to_arr
inventory = csv_to_arr('kepemilikan','save0')
games = csv_to_arr('game','save0')
search_my_game(inventory,games,0)