#main
import argparse
import os
import sys
import f_csvparser as csvparser
import f_common as common
import f02 as f02
import f03 as f03
import f04 as f04
import f05 as f05
import f06 as f06
import f07 as f07
import f08 as f08
import f09 as f09
import f10 as f10
import f11 as f11
import f12 as f12
import f13 as f13
import f14 as f14
import f15 as f15
import f16 as f16
import f17 as f17

# KAMUS GLOBAL
# variabel array dari csv : game; kepemilikan; riwayat; user



# LOAD
parser = argparse.ArgumentParser()
parser.add_argument('folder',type=str)

args = parser.parse_args()

path = '.\\saves\\' + args.folder # path folder
isFolderExist = os.path.exists(path) # cek apakah folder ada

if args.folder=='':
    print("Tidak ada nama folder yang diberikan!")
    print('Usage: python bnmo_main.py <nama_folder>')
else:
    if not isFolderExist:
        print('Folder', '"%s"' % args.folder, 'tidak ditemukan.')
    else:
        user,game,riwayat,kepemilikan = f15.load(args.folder)
               
        # meminta perintah
        call_func = False
        while not call_func:
            functions = input(">>> ")
            if functions == 'register':
                user = f02.register(user)
            elif functions == 'login':
                user_id = f03.login()
                #userinventory = common.create_inventory_arr(kepemilikan, game, user_id)
                #tokogame = common.create_tokogame_arr(game)
                #userhistory = common.create_userhistory_arr(riwayat, user_id)
                # kalau belum bisa login, hanya bisa panggil perintah login saja
            #elif functions=='tambah_game':
            #    f04.tambah_game(game)
            #elif functions=='ubah_game':
            #    f05.ubah_game(game)
            #elif functions=='ubah_stok':
            #    f06.ubah_stok(game)
            #elif functions=='list_game_toko':
            #    f07.list_game_toko(game)
            #elif functions=='buy_game':
            #    f08.buy_game(user,game,kepemilikan,riwayat,userinventory,user_id)
            #elif functions=='list_game':
            #    f09.list_game(userinventory)
            #elif functions=='search_my_game':
            #    f10.search_my_game(userinventory)
            #elif functions=='search_game_at_store':
            #    f11.search_game_at_store(tokogame)
            #elif functions=='topup':
            #    f12.topup(user)
            #elif functions=='riwayat':
            #    f13.riwayat()
            #elif functions=='help':
            #    f14.Help()
            #elif functions=='save':
            #    f16.save(user,game,kepemilikan,riwayat)
            #elif functions=='exit':
            #    f17.bnmo_exit()
        
        
        
        
        



# tes
#kepemilikan = csvparser.csv_to_arr('kepemilikan', 'save0')
#game = csvparser.csv_to_arr('game', 'save0')
#riwayat = csvparser.csv_to_arr('riwayat', 'save0')
#user = csvparser.csv_to_arr('user', 'save0')


#userinventory = common.create_inventory_arr(kepemilikan, game, 0) # admin id 0
#tokogame = common.create_tokogame_arr(game)
#userhistory = common.create_userhistory_arr(riwayat, 0)
#sebelum
#print('sebelum')
#for i in range(1, common.iterLength(user)):
#    print(user[i])
#print()

#print('hasil penambahan')
#user = f12.topup(user)
#for i in range(1, common.iterLength(user)):
#    print(user[i])
#for i in range(common.iterLength(userhistory)):
#   print(userhistory[i])
#print()

#f08.beli_game(user,game,kepemilikan,riwayat,userinventory,0)

# f09.list_game(userinventory)
