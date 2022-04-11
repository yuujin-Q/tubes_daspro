# Common Functions/Procedures:
# iterLength(iterable)        menyerupai fungsi len()
# strSplit(str, delimiter=' ')      mirip dengan fungsi .split()
# ...

# fungsi iterLength
def iterLength(iterable):
    i = 0
    while True:     # pengulangan dilakukan hingga terjadi error dalam mengakses iterable
        try:
            if iterable[i] is not None:     # jika tidak error, penghitung i diincrement
                i+=1
        except:     # jika error, fungsi diselesaikan
            return i


# fungsi strSplit
def strSplit(str, delimiter = None):    # berfungsi sama dengan fungsi .split() tanpa parameter maxsplit
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
    elif not noDelim:
        strSplitResult += [tempstr]
    
    return strSplitResult   # return array hasil
