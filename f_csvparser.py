'''
FUNGSI CSV PARSER
Spesifikasi : 
I.S.: file csv
F.S.: variabel user, game, riwayat, kepemilikan dengan tipe array of array
'''

# KAMUS LOKAL
# filename, folder, filedir : string
# file : csv file
# lines : function readlines
# user, game, riwayat, kepemilikan : array of array

# ALGORITMA
# IMPORT MODULE
import f_common as common

# REALISASI FUNGSI
def csv_to_arr(filename, folder):
    arr = []

    if filename == 'user':
        filedir = '.\\'+folder+'\\user.csv'
    elif filename == 'game':
        filedir = '.\\'+folder+'\\game.csv'
    elif filename == 'riwayat':
        filedir = '.\\'+folder+'\\riwayat.csv'
    elif filename == 'kepemilikan':
        filedir = '.\\'+folder+'\\kepemilikan.csv'
    
    file = open(filedir,'r')
    lines = file.readlines()

    for line in lines:
        temprow = []
        templine = ""
        for i in range(common.strLength(line) - 1):     # untuk menghapus escape character newline pada line ('\n')
            templine += line[i]
        temprow = common.strSplit(templine, ',')
        arr += [temprow]
    return arr

# filename = input()
# folder = input()
# print(csv_to_arr(filename,folder))