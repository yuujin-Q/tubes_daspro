# Common Functions/Procedures:
# iterLength(iterable)        menyerupai fungsi len()
# strSplit(str, delimiter=' ')      mirip dengan fungsi .split()
# arr_to_str(arr, delim)    memisahkan sebuah array menjadi string yang berisi setiap elemen array, yang dibatasi delimiter
# arrarr_to_str(arrarr, delim)  mirip seperti arr_to_str(arr, delim), tetapi berfungsi untuk memisahkan array of array
# alignTable(arr)       mengembalikan arr (array of array) yang lebar kolomnya disamakan dengan penambahan spasi ' '
# create_inventory_arr(kepemilikan, game, userid)   menghasilkan array yang berisi data kepemilikan (inventory game)
# create_tokogame_arr(game)     menghasilkan array yang berisi data game di toko
# 
# remove_thousands(numstr)      menghasilkan string numerik dari string numerik yang memiliki pemisah ribuan '.'
# ...

# fungsi iterLength
def iterLength(iterable):
    # SPESIFIKASI: menghasilkan panjang dari sebuah array atau string (tipe iterable)
    # KAMUS LOKAL:
        # i : integer
    # ALGORITMA:
    i = 0
    while True:     # pengulangan dilakukan hingga terjadi error dalam mengakses iterable
        try:
            if iterable[i] is not None:     # jika tidak error, penghitung i diincrement
                i+=1
        except:     # jika error, fungsi diselesaikan
            return i


# fungsi strSplit
def strSplit(str, delimiter = None):
    # SPESIFIKASI: memisahkan string yang berisi delimiter menjadi sebuah array; berfungsi sama dengan fungsi .split() tanpa parameter maxsplit
    # KAMUS LOKAL:
        # strSplitResult : array of string
        # strLen, i : integer
        # tempstr : string
        # noDelim : boolean
    # ALGORITMA:

    # apabila parameter delimiter tidak dimasukkan (None), maka strSplit akan memisahkan str menjadi beberapa string yang bukan ' ' 
    strSplitResult = []
    strLen = iterLength(str)
    i = 0
    tempstr = ""
    if delimiter is None:
        noDelim = True
        delimiter = " "
    else:
        noDelim = False

    for i in range(strLen):     # pemisahan string dengan delimiter
        if str[i] != delimiter:
            tempstr += str[i]
        elif str[i] == delimiter:
            if noDelim:
                if tempstr!= "":
                    strSplitResult += [tempstr]
                tempstr = ''
            else:
                strSplitResult += [tempstr]
                tempstr = ''
    
    # penambahan hasil split yang tertinggal
    if tempstr != '':
        strSplitResult += [tempstr]
    elif not noDelim:           # khusus untuk pemanggilan dengan delimiter, delimiter pada ujung baris menyebabkan penambahan ''
        strSplitResult += [tempstr]
    
    return strSplitResult   # return array hasil


def arr_to_str(arr, delim):
    # SPESIFIKASI: menghasilkan sebuah string, yang dipisahkan delimiter (parameter delim), dari sebuah array (parameter arr)
    # KAMUS LOKAL:
        # strResult : string
        # colcount : integer
        # j : integer
    # ALGORITMA:
    strResult = ""
    colcount = iterLength(arr)     # jumlah kolom data
    for j in range(colcount):   # pemrosesan traversal kolom
        strResult += str(arr[j])
        if j < colcount - 1:
            strResult += delim          # penambahan delimiter setelah sebuah elemen dari array
    return strResult


def arrarr_to_str(arrarr, delim):
    # SPESIFIKASI: menghasilkan sebuah string, yang dipisahkan delimiter (parameter delim), dari sebuah array of array (parameter arrarr)
    # KAMUS LOKAL:
        # strResult : string
        # rowcount : integer
        # i : integer
    # ALGORITMA:
    strResult = ""
    rowcount = iterLength(arrarr)        # jumlah baris data
    for i in range(rowcount):       # pemrosesan traversal baris
        strResult += arr_to_str(arrarr[i],delim)
        strResult += '\n'         # penambahan '\n' pada akhir baris
    return strResult

def alignTable(arr):
    # SPESIFIKASI : merapikan output tabel (array); I.S: arr terdefinisi dan jumlah baris>1 (indeks pertama nol)
    # KAMUS LOKAL
        # arr : array of string
        # maxlength : array of int

    # ALGORITMA
    maxlength = []      # array yang berisi panjang string maksimum pada sebuah kolom
    for col in range(iterLength(arr[0])):     # pencarian panjang maksimum pada kolom
        colmax = iterLength(arr[0][col])
        for row in range(iterLength(arr)):
            if iterLength(arr[row][col]) > colmax:
                colmax = iterLength(arr[row][col])
        maxlength += [colmax]
    
    # menambahkan spasi pada elemen sehingga panjang setiap elemen sama
    for row in range(iterLength(arr)):
        for col in range(iterLength(arr[row])):
            arr[row][col] += (maxlength[col] - iterLength(arr[row][col])) * " "
    
    return arr

def create_inventory_arr(kepemilikan, game, userid):
    # SPESIFIKASI: menghasilkan array yang berisi data game yang dimiliki seorang user
    # KAMUS LOKAL:
        # user_inventory : array of array
        # i, j : integer
    # ALGORITMA:
    user_inventory = []

    if iterLength(kepemilikan)>1:
        userid = str(userid)
        for i in range(1,iterLength(kepemilikan)):     # membuat array yang berisi id dari game-game yang dimiliki seorang user
            if kepemilikan[i][1] == userid:
                user_inventory += [kepemilikan[i][0]]
        for i in range(iterLength(user_inventory)):      # menambahkan data game dari toko berdasarkan id yang baru disimpan dalam array user_inventory
            for j in range(1, iterLength(game)):
                if user_inventory[i] == game[j][0]:
                    user_inventory[i] = [game[j][0], game[j][1], game[j][4], game[j][2], game[j][3]]
    return user_inventory

def create_tokogame_arr(game):
    # SPESIFIKASI: menghasilkan array yang berisi data game yang dimiliki seorang user
    # KAMUS LOKAL:
        # tokogame : array of array
        # j : integer
    # ALGORITMA:
    tokogame = []

    if iterLength(game)>1:
        for j in range(1, iterLength(game)):   # membuat baris pada tokogame
            tokogame += [[game[j][0], game[j][1], game[j][4], game[j][2], game[j][3], game[j][5]]]
    return tokogame

def create_userhistory_arr(riwayat, userid):
    # SPESIFIKASI: menghasilkan array yang berisi data riwayat pembelian game oleh seorang user
    # KAMUS LOKAL:
        # userhistory : array of array
        # j : integer
    # ALGORITMA:
    userhistory = []

    if iterLength(riwayat)>1:
        for j in range(1, iterLength(riwayat)):   # membuat baris pada tokogame
            if str(userid) == riwayat[j][3]:
                userhistory += [[riwayat[j][0], riwayat[j][1], riwayat[j][2], riwayat[j][4]]]
    return userhistory


def remove_thousands(numstr):
    # SPESIFIKASI: menerima string numerik yang berisi pemisah ribuan '.' dan mengembalikan sebagai string numerik saja
    # KAMUS LOKAL:
        # arr_to_str(arr : array of string; delim : string) -> string
        # strSplit(str: string; delimiter : string or null) -> array
    # ALGORITMA:
    numstr = arr_to_str(  strSplit(numstr, '.') ,'' )
    return numstr