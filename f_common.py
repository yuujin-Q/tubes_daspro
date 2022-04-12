# Common Functions/Procedures:
# iterLength(iterable)        menyerupai fungsi len()
# strSplit(str, delimiter=' ')      mirip dengan fungsi .split()
# arr_to_str(arr, delim)    memisahkan sebuah array menjadi string yang berisi setiap elemen array, yang dibatasi delimiter
# arrarr_to_str(arrarr, delim)  mirip seperti arr_to_str(arr, delim), tetapi berfungsi untuk memisahkan array of array
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
