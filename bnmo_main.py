# Program BNMO
# Spesifikasi : Program BNMO adalah program dengan sistem inventarisasi dan toko game

# KAMUS GLOBAL
    # VARIABEL
        # parser : argparse argument folder : string
        # path : string
        # isFolderExist, call_func, logged_in : boolean
        # user,game,riwayat,kepemilikan : array of array of string
        # functions : string
        # user_id : string
        # userinventory, tokogame, userhistory : array of array of string
        # isAdmin : boolean
        # 

# ALGORITMA
# IMPORT MODUL
import argparse
import os
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

# LOAD
parser = argparse.ArgumentParser()
parser.add_argument('folder',nargs='?',type=str, default='')

#parser.add_argument('folder',type=str,action='store_true')
#args = parser.parse_args()
#if not args.folder:
#    print('Tidak ada folder yang diberikan')
#else:
#    path = '.\\saves\\' + args.folder # path folder
#    isFolderExist = os.path.exists(path) # cek apakah folder ada
#    #parser.parse_args('folder')
#    # if args.folder is not None:
#    if not isFolderExist:
#        print('Folder', '"%s"' % args.folder, 'tidak ditemukan.')
#    else:
#        user,game,riwayat,kepemilikan = f15.load(args.folder)

args = parser.parse_args()
if args.folder != '': 
    path = '.\\saves\\' + args.folder # path folder
    isFolderExist = os.path.exists(path) # cek apakah folder ada

    if not isFolderExist:
        print('Folder', '"%s"' % args.folder, 'tidak ditemukan.')
    else:
        user,game,riwayat,kepemilikan= f15.load(args.folder)

        # meminta perintah
        funcs = ['login', 'register', 'tambah_game', 'ubah_game', 
        'ubah_stok', 'list_game_toko', 'buy_game', 'list_game', 
        'search_my_game', 'search_game_at_store','topup','riwayat',
        'help','save','exit']
        call_func = False
        logged_in = False
        user_role=''
        while not call_func:
            functions = input(">>> ")

            for i in range(common.iterLength(funcs)):
                if funcs[i] == functions:
                    validfunc = True
                    break
                else:
                    validfunc = False

            if functions == 'login':   # f03.login(user)
                if not logged_in:
                    logged_in,user_id = f03.login(user)
                    user_role = user[user_id][4]
                else:
                    print("Halo " + user[user_id][2] + "! Selamat datang di " + '"%s"' % "Binomo" + ".")
            
            elif functions=='help':     # f14
                f14.Help(user_role)
            
            elif functions=='exit':     # f17
                call_func=f17.bnmo_exit(user,game,riwayat,kepemilikan)

            elif logged_in and validfunc:
                userinventory = common.create_inventory_arr(kepemilikan, game, user_id)
                tokogame = common.create_tokogame_arr(game)
                userhistory = common.create_userhistory_arr(riwayat, user_id)
                
                if functions == 'register' and user_role=='Admin':     # f02
                    user = f02.register(user)
            
                elif functions=='tambah_game' and user_role=='Admin':    # f04
                    game = f04.tambah_game(game)
                
                elif functions=='ubah_game'and user_role=='Admin':     # f05
                    game = f05.ubah_game(game)
                
                elif functions=='ubah_stok'and user_role=='Admin':     # f06
                    game = f06.ubah_stok(game)
                
                elif functions=='list_game_toko':     # f07
                    f07.list_game_toko(tokogame)
                
                elif functions=='buy_game' and user_role=='User':     # f08
                    game,riwayat,kepemilikan=f08.buy_game(user,game,riwayat,kepemilikan,userinventory,user_id)
                
                elif functions=='list_game' and user_role=='User':     # f09
                    f09.list_game(userinventory)

                elif functions=='search_my_game' and user_role=='User':     # f10
                    f10.search_my_game(userinventory)

                elif functions=='search_game_at_store':     # f11
                    f11.search_game_at_store(tokogame)
                
                elif functions=='topup' and user_role=='Admin':     # f12
                    user = f12.topup(user)
                
                elif functions=='riwayat' and user_role=='User':     # f13
                    f13.riwayat(user_id,userhistory, kepemilikan)

                elif functions=='save':     # f16
                    f16.save(user,game,riwayat,kepemilikan)
                               
                else:
                    if user_role=='Admin':
                        print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
                    else:
                        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
                    
            else: # kalau belum login, hanya bisa panggil perintah login saja
                if validfunc:
                    print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain", '"%s"' % "login")
                else:
                    print('Perintah tidak valid. Ketik "help" untuk membaca panduan')
else:
    print("Tidak ada nama folder yang diberikan!")
    print('Usage: python bnmo_main.py <nama_folder>')

