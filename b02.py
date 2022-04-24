'''
B02 - Kerang Ajaib
Spesifikasi : Permainan kerang ajaib
Coder : 16521316
'''

import time
import f_common as common

def lcgmethod(seed_data):
    lastindex = common.iterLength(seed_data)-1
    m = int(time.time()) // int(time.time())-999
    a = int(time.time()) // int(time.time())-666
    c = int(time.time()) // int(time.time())-333

    new_seed = (a*seed_data[lastindex] + c) % m
    return new_seed


def conch_shell(randomseeddata):
    randomseeddata += [lcgmethod(randomseeddata)]
    lastindex = common.iterLength(randomseeddata)-1

    outputoption = randomseeddata[lastindex] % 8
    q = input('Apa pertanyaanmu? ')

    if outputoption == 0:
        print('Bisa Jadi.')
    elif outputoption == 1:
        print('Tidak tau.')
    elif outputoption == 2:
        print('Mungkin.')
    elif outputoption == 3:
        print('Tidak mungkin.')
    elif outputoption == 4:
        print('Tentu saja iya.')
    elif outputoption == 5:
        print('Tentu saja tidak.')
    elif outputoption == 6:
        print('Iya.')
    elif outputoption == 7:
        print('Tidak.')
    
    return randomseeddata



