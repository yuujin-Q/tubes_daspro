'''
FUNGSI CSV PARSER
Spesifikasi : 
I.S.: file csv
F.S.: variabel user, game, riwayat, kepemilikan dengan tipe array of array
'''

# KAMUS LOKAL
# filename, folder, filepath : string
# file : text csv file
# lines : list of string; hasil function readlines
# line : string; string individual dari lines
# templine : string; pemrosesan terhadap line
# strlen: int: panjang line
# i : int; indeks traversal
# temprow : array of string; penambahan baris dalam arr
# arr : array of array of string; hasil akhir parsing csv


# ALGORITMA
# IMPORT MODULE
import f_common as common

# REALISASI FUNGSI
def csv_to_arr(filename, folder):
    arr = []

    filepath = '.\\saves\\' + folder + '\\' + filename + '.csv'
    
    file = open(filepath,'r')
    lines = file.readlines()
    file.close()

    for line in lines:
        temprow = []
        templine = ""
        strlen = common.iterLength(line)
        for i in range(strlen):     # untuk menghapus escape character newline pada line ('\n')
            if i < strlen:
                if line[i] == "\n":
                    break
            templine += line[i]
        temprow = common.strSplit(templine, ';')  # pemisahan temprow dengan delimiter ';'
        arr += [temprow]        # penambahan baris (temprow) ke hasil
    return arr
