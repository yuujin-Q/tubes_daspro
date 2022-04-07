# Common Functions/Procedures:
# strLength(str)        menyerupai fungsi len()
# strSplit(str, delimiter=' ')      mirip dengan fungsi .split()


# fungsi strLength
def strLength(str):     # ekuivalen dengan len() untuk string
    str += '爱'  # sentinel 爱
    count = 0
    while str[count] != '爱':
        count+=1
    return count        

def strSplit(str, delimiter = None):    # berfungsi sama dengan fungsi .split() tanpa parameter maxsplit
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
    
    if tempstr != '':       # mengecek hasil split yang tertinggal
        strSplitResult += [tempstr]
    elif not noDelim:
        strSplitResult += [tempstr]
    return strSplitResult

print(strSplit(input()))

