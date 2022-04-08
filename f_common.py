# Common Functions/Procedures:
# strLength(str)        menyerupai fungsi len()
# strSplit(str, delimiter=' ')      mirip dengan fungsi .split()
# ...

# fungsi strLength
def strLength(str):     # ekuivalen dengan len() untuk string
    str += '爱'  # sentinel 爱
    count = 0
    while str[count] != '爱':   # mengecek secara iteratif apakah char pada array of char (string) adalah sentinel
        count+=1
    return count        # return jumlah karakter yang bukan sentinel        

def strSplit(str, delimiter = None):    # berfungsi sama dengan fungsi .split() tanpa parameter maxsplit
    # apabila parameter delimiter tidak dimasukkan (None), maka strSplit akan memisahkan str menjadi beberapa string yang bukan ' ' 
    strSplitResult = []
    strLen = strLength(str)
    i = 0
    tempstr = ""
    if delimiter is None:
        noDelim = True
        delimiter = " "
    else:
        noDelim = False

    for i in range(strLen):
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
