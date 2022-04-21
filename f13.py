'''
MODUL F13-Melihat Riwayat Pembelian
Spesifikasi : Memberikan daftar riwayat game yang pernah dibeli.
I.S. : command riwayat
F.S. : daftar riwayat game dengan format tertentu
Desainer dan coder : 16521262, 16521199
'''
# KAMUS LOKAL
    # ada_riwayat : boolean
    # i : integer
# ALGORITMA
# IMPORT FUNGSI
import f_common as common

# REALISASI FUNGSI
def riwayat(user_id, userhistory, kepemilikan):
    
    # mengecek apakah user memiliki game (pernah melakukan pembelian)
    ada_riwayat = False
    for i in range(common.iterLength(kepemilikan)):
        if user_id == kepemilikan[i][1]:
            ada_riwayat = True
    
    # jika user tidak memiliki game (belum pernah melakukan pembelian)
    if ada_riwayat == False:
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")
    
    #jika user pernah melakukan pembelian
    if ada_riwayat == True:
        # mengeluarkan output berupa list game yang dimiliki user
        print("Daftar game: ")
        userhistory = common.alignTable(userhistory)    # merapikan string dalam array
        for i in range(common.iterLength(userhistory)):
            print(f'{i+1}. ' + common.arr_to_str(userhistory[i],' | '))    # mencetak sesuai format

