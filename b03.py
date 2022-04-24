'''
B03 - GAME TIC-TAC-TOE
Spesifikasi : Permainan tic-tac-toe dari sembilan petak
Coder : 16521316, 16521172
'''

# KAMUS
    # FUNGSI DAN PROSEDUR
        # checkwin (papan : array of array of string) -> boolean   { mengecek apakah sudah ada yang menang atau belum }
        # validasi (X,Y: string, papan : array of array of string) -> boolean   { mengecek apakah input valid }
        # printpapan (input papan : array of array of string)   { mencetak papan tic-tac-toe ke layar }
        # giliran (pemain : string, papan : array of array of string) -> array of array of string   { Meminta input pada giliran pemain }

# ALGORITMA
# REALISASI FUNGSI DAN PROSEDUR
def checkwin(papan):
    # Spesifikasi : Mengecek apakah sudah ada yang menang atau belum
    # KAMUS LOKAL
        # i,j : integer
    # ALGORITMA
    for i in range(1,4):
        if papan[i][1]+papan[i][2]+papan[i][3]=='XXX' or papan[i][1]+papan[i][2]+papan[i][3]=='OOO':
            return True
    for j in range(1,4):
        if papan[1][j]+papan[2][j]+papan[3][j]=='XXX' or papan[1][j]+papan[2][j]+papan[3][j]=='OOO':
            return True
    if papan[1][1]+papan[2][2]+papan[3][3]=='XXX' or papan[1][1]+papan[2][2]+papan[3][3]=='OOO':
        return True
    elif papan[1][3]+papan[2][2]+papan[3][1]=='XXX' or papan[1][3]+papan[2][2]+papan[3][1]=='OOO':
        return True
    else:
        return False

def validasi(X,Y,papan):
    # Spesifikasi : mengecek apakah input valid
    # KAMUS LOKAL
    simbol = '#'   # constant simbol : string = '#'
    # ALGORITMA
    if X < 1 or X > 3 or Y < 1 or Y > 3:
        print('Kotak tidak valid.')
        return False
    elif papan[X][Y] != simbol:
        print('Kotak sudah terisi. Silakan pilih kotak lain.')
        return False
    else:
        return True
    
def printpapan(papan):
    # Spesifikasi : Mencetak papan ke layar
    # KAMUS LOKAL
        # row : integer
    # ALGORITMA
    for row in range (1,4):
        print(papan[row][1]+papan[row][2]+papan[row][3])

def giliran(pemain, papan):
    # Spesifikasi : Meminta input pada giliran pemain
    # KAMUS LOKAL
        # valid : boolean
        # X,Y : string
    # ALGORITMA
    print(f"Giliran Pemain {pemain}")
             
    valid = False
    while not valid:
        X = int(input("Baris: "))
        Y = int(input("Kolom: "))
        valid = validasi(X,Y, papan)
    papan[X][Y] = pemain

    print("Status Papan")
    printpapan(papan)
    print()
    return papan

# REALISASI PROSEDUR UTAMA
def tictactoe():
    # output keterangan awal
    print("Legenda:")
    print("# Kosong")
    print("X Pemain 1")
    print("O Pemain 2")
    print()
    print("Status Papan")
    
    papan = [['#' for col in range (4)] for row in range (4)]   # membuat array papan
    
    printpapan(papan)   # cetak papan ke layar
    print()
    
    win = False
    langkah = 0
    while not win and langkah <= 9:   # game dimulai
        papan = giliran('X', papan)   # meminta giliran pemain X
        langkah += 1   # langkah ditambahkan satu
        win = checkwin(papan)   # cek apakah pemain X menang atau tidak
        if win:   # jika pemain X menang
            print('Pemain "X" menang!')
        elif langkah < 9:   # jika belum menang dan langkah masih valid (< 9)
            papan = giliran('O', papan)   # meminta giliran pemain Y
            langkah += 1   # langkah ditambahkan satu
            win = checkwin(papan)   # cek apakah pemain Y menang atau tidak
            if win:   # jika pemain Y menang
                print('Pemain "O" menang!')
        else: # jika langkah ke-9 dan belum ada yang menang
            break
                
    if not checkwin(papan) and langkah >= 9:   # jika langkah ke-9 dan belum ada yang menang
        print("Seri. Tidak ada pemenang.")   # permainan seri
# tictactoe()