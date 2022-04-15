'''
MODUL F09-Melihat Game yang dimiliki
Spesifikasi : Memberikan daftar game yang dimiliki pengguna
I.S. : command
F.S. : data game
Desainer dan coder : 16521262, 16521199
'''

# ALGORITMA
import f_common as common

# REALISASI FUNGSI
def list_game(user_inventory):
        
    # search
    count = 0
    search_result = []      # array hasil pencarian
    for i in range(1, common.iterLength(user_inventory)):
        count +=1
        search_result += [user_inventory[i]] 
        search_result = [user_inventory[i][0], user_inventory[i][1], user_inventory[i][2], user_inventory[j][3], user_inventory[j][4]]
        
    # output
    if count == 0: # tidak ada game
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
    else:       # minimal ada satu game
        print("Daftar game:")
        search_result = common.alignTable(search_result)        # menyejajarkan posisi string dalam array
        for i in range(common.iterLength(search_result)):
            print(f'{i+1}. ' + common.arr_to_str(search_result[i],' | ')) # output dalam bentuk tabel yang sudah rapi
