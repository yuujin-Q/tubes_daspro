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

# ALGORITMA
# IMPORT MODUL
from operator import inv
import f16
from f_csvparser import csv_to_arr

# REALISASI FUNGSI
def search_my_game():
    id_game = input("Masukkan ID Game: ")
    tahun_rilis = int(input("Masukkan Tahun Rilis Game: "))
    print()
    print("Daftar game pada inventory-mu yang memenuhi kriteria:")
    
    # deklarasikan array file kepemilikan.csv
    inventory = csv_to_arr('kepemilikan','csv_files')
    games = csv_to_arr('game','csv_files')
    
    # search
    count_search = 0
    if id_game=="":
        for j in range(len(games)):
            if j>0 and tahun_rilis == int(games[j][3]):
                for i in range (len(inventory)):
                    if inventory[i][0] == games[j][0]:
                        print(games[j][0] + " | " + games[j][1] + " | " + games[j][4] + " | " + games[j][5] + " | " + str(tahun_rilis))
                        count_search+=1
        if count_search==0:
            print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
    else:
        for i in range (len(inventory)):
            if id_game == inventory[i][0]:
                for j in range (len(games)):
                    if id_game == games[j][0] and tahun_rilis == int(games[j][3]):
                        print(games[j][0] + " | " + games[j][1] + " | " + games[j][4] + " | " + games[j][5] + " | " + str(tahun_rilis))
                        count_search+=1
        
            elif i==(len(inventory)-1) and count_search==0: #tidak ada game yang cocok
                print("Tidak ada game pada inventory-mu yang memenuhi kriteria")