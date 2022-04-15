#main
import f_csvparser as csvparser
import f_common as common
# import f02 as f02
# import f03 as f03
import f04 as f04
# import f05 as f05
import f06 as f06
import f07 as f07
# import f08 as f08
# import f09 as f09
import f10 as f10
# import f11 as f11
# import f12 as f12
# import f13 as f13
# import f14 as f14
# import f15 as f15
# import f16 as f16
# import f17 as f17

# KAMUS GLOBAL
# variabel array dari csv : game; kepemilikan; riwayat; user

# f07 prosedur



kepemilikan = csvparser.csv_to_arr('kepemilikan', 'save0')
game = csvparser.csv_to_arr('game', 'save0')

tokogame = common.create_tokogame_arr(game)
#sebelum
for i in range(common.iterLength(tokogame)):
    print(tokogame[i])
print()

f07.list_game_toko(tokogame)