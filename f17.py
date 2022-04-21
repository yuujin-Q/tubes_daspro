# Modul F17-Exit
# prosedur: keluar dari program
import f16 as f16


def bnmo_exit(user,game,riwayat,kepemilikan):
    # SPESIFIKASI: mengeluarkan pengguna dari program; fungsi ini akan menanyakan pengguna apakah ingin melakukan save
    # KAMUS LOKAL:
        # choice : string
    # ALGORITMA:
    choice = 'a'
    while not(choice =='y' or choice=='n'):
        choice= input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ").lower()
    if choice == 'y':
        f16.save(user,game,riwayat,kepemilikan)
    return True

# f_exit()