#fungsi untuk melihat riwayat pembelian user
def riwayat():
    #user g punya riwayat pembelian
    print("Maaf, kamu tidak ada rowayat pebelian game. Ketik perintah beli_game untuk membeli.")
    #kl punya 
    print("Daftar game: ")
    #dll
 
'''
MODUL F13-Melihat Riwayat Pembelian
Spesifikasi : Memberikan daftar riwayat game yang pernah dibeli.
I.S. : 
F.S. : 
Desainer dan coder : 16521262, 16521199
'''

'''
def riwayat():
    #mengecek apakah user punya riwayat pembelian
    #cek apakah user id ada di file riwayat.csv
    ada_riwayat = False
    for column in file:
        if userid == column[3]:
            ada_riwayat = True
    #jika tidak ada
    if ada_riwayat == False
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")
    #jika ada 
    if ada_riwayat == True
    print("Daftar game: ")

'''
'''
game_id;nama;harga;user_id;tahun_beli
ID | Nama game | Harga | Tahun Beli |

'''
'''

# filter user id
    sum = 0
    search_result = []      # array hasil pencarian
    for i in range(common.iterLength(user_inventory)):
        if userid = user_id :
            sum +=1
            search_result += [user_inventory[i]]
        else:       # tidak ada user id dalam riwayat.csv
             print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")
            
    # output
    if count == 0: # tidak ada game
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
    else:       # minimal ada satu game
        search_result = common.alignTable(search_result)        # menyejajarkan posisi string dalam array
        for i in range(common.iterLength(search_result)):
            print(f'{i+1}. ' + common.arr_to_str(search_result[i],' | ')) # output dalam bentuk tabel yang sudah rapi

'''
