'''
MODUL F10-Mencari Game yang Dimiliki dari ID dan Tahun Rilis
Spesifikasi: Mencari game yang dimiliki dari ID dan tahun rilis
I.S. : input id dan tahun rilis game yang ingin dicari
F.S. : output data game tersebut
Desainer dan coder : 16521172, 16521316
'''

# KAMUS LOKAL
    # FUNGSI DAN PROSEDUR
        # common.iterLength(iterable: string or array) -> integer
        # common.alignTable(input/output arr : array of array of string)
        # common.arr_to_str(arr : array; delim : string) -> string
    # VARIABEL
        # user_inventory : array of array of string
        # id_game, tahun_rilis : string
        # count : int
        # id, tahun: boolean
        # i, j : integer
        # search_result : array of array of string 
# 

# ALGORITMA
import f_common as common

# REALISASI FUNGSI
def search_my_game(inventory, games, userid):
    user_inventory = []
    userid = str(userid)
    for i in range(1,common.iterLength(inventory)):     # membuat array yang berisi id dari game-game yang dimiliki seorang user
        if inventory[i][1] == userid:
            user_inventory += [inventory[i][0]]
    for i in range(common.iterLength(user_inventory)):      # menambahkan data game dari toko berdasarkan id yang baru disimpan dalam array user_inventory
        for j in range(1, common.iterLength(games)):
            if user_inventory[i] == games[j][0]:
                user_inventory[i] = [games[j][0], games[j][1], games[j][4], games[j][2], games[j][3]]
    
    # input dari user
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
    count = 0
    search_result = []      # array hasil pencarian
    for i in range(common.iterLength(user_inventory)):
        if id and tahun: # jika input kedua parameter kosong
            count +=1
            search_result += [user_inventory[i]]
        else:       # setidaknya satu input tidak kosong
            if (id_game == user_inventory[i][0] and tahun) or (tahun_rilis == user_inventory[i][4] and id) or (id_game == user_inventory[i][0] and tahun_rilis== user_inventory[i][4]):
                count +=1
                search_result += [user_inventory[i]]
    # output
    if count == 0: # tidak ada game
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
    else:       # minimal ada satu game
        search_result = common.alignTable(search_result)        # menyejajarkan posisi string dalam array
        for i in range(common.iterLength(search_result)):
            print(f'{i+1}. ' + common.arr_to_str(search_result[i],' | ')) # output dalam bentuk tabel yang sudah rapi
