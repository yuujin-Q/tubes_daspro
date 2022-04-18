'''
MODUL F09-Melihat Game yang dimiliki
Spesifikasi : Memberikan daftar game yang dimiliki pengguna
I.S. : command
F.S. : data game
Desainer dan coder : 16521262, 16521199
'''

# KAMUS LOKAL
    #FUNGSI DAN PROSEDUR
        # common.iterLength(iterable: string or array) -> integer
        # common.alignTable(input/output arr : array of array of string)
        # common.arr_to_str(arr : array; delim : string) -> string
    #VARIABEL
        # user_inventory : array of array of string
        # count : int
        # i : integer

# ALGORITMA
import f_common as common

# REALISASI FUNGSI
def list_game(user_inventory):
    
    # search
    count = common.iterLength(user_inventory)
    for i in range(count):
        user_inventory[i] = [user_inventory[i][0], user_inventory[i][1], user_inventory[i][3], user_inventory[i][4], user_inventory[i][2]]
    
    # output
    if count == 0: # tidak ada game
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
    else:       # minimal ada satu game
        print("Daftar game:")
        
        user_inventory = common.alignTable(user_inventory)        # menyejajarkan posisi string dalam array
        for i in range(count):
            print(f'{i+1}. ' + common.arr_to_str(user_inventory[i],' | ')) # output dalam bentuk tabel yang sudah rapi
