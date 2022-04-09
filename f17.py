# Modul F17-Exit
# prosedur: keluar dari program

def exit():
    pass
    choice = 'a'
    while not(choice =='y' or choice=='n'):
        choice=input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if choice == 'y':
        pass
        #f16 save
    else:  # choice =='n'
        exit()