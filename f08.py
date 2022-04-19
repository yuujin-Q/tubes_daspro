'''
MODUL F08-Membeli Game
Spesifikasi: Membeli game sehingga game masuk ke dalam data kepemilikan (inventory) user
I.S. : input id game yang ingin dibeli
F.S. : kepemilikan dan riwayat diupdate jika game berhasil dibeli atau tidak mengembalikan apa-apa jika game gagal dibeli
Desainer dan coder : 16521172, 16521262
'''

# KAMUS LOKAL
    # FUNGSI DAN PROSEDUR
        # common.iterLength(iterable: string or array) -> integer
        # common.remove_thousands(numstr : string) -> string
    # VARIABEL
        # i : integer
        # id_game : string
        # found : boolean

# ALGORITMA
# IMPORT FUNGSI
import f_common as common
import datetime

# REALISASI FUNGSI
def beli_game (user,game,kepemilikan,riwayat,user_inventory,user_id):
    id_game = input("Masukkan ID Game: ")   # input dari pengguna
    
    # mencari id game di game.csv
    found = False   # definisikan boolean game belum ditemukan
    for i in range (common.iterLength(user_inventory)):   # cek array kepemilikan pengguna
        if id_game == user_inventory[i][0]:   # jika game sudah pernah dibeli (ada di user_inventory)
            print("Anda sudah memiliki Game tersebut")
            found = True   # game ditemukan
    
    if found == False:   # jika game belum pernah dibeli (tidak ada di user_inventory)
        for i in range (1,common.iterLength(game)):   # cek game.csv
            if id_game == game[i][0] and int(game[i][5])>0:   # mencari id game dan jika stok game > 0
                if int(common.remove_thousands(game[i][4])) <= int(user[user_id+1][5]):   # jika saldo user cukup
                    print("Game " + '"%s"' % id_game + " berhasil dibeli!")
                    kepemilikan += [[id_game,str(user_id)]]   # menambahkan data game ke kepemilikan
                    riwayat += [[id_game,game[i][1],game[i][4],str(user_id),datetime.date.today().year]]   # menambahkan data game ke riwayat
                else:   # jika saldo user tidak cukup
                    print("Saldo anda tidak cukup untuk membeli Game tersebut!")
            elif id_game == game[i][0]:   # jika stoknya nol (0)
                print("Stok Game tersebut sedang habis!")
                break
            
    return kepemilikan, riwayat
