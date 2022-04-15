'''
MODUL F07-Listing Game di Toko Berdasarkan ID, Tahun Rilis dan Harga
Spesifikasi: mencetak isi array tokogame dalam urutan yang diinginkan
I.S. : tokogame terdefinisi, urutan sembarang
F.S. : isi tokogame berhasil dicetak dengan urutan yang diinginkan
Desainer dan coder : 16521262, 16521316
'''

import f_common as common

def list_game_toko(tokogame):
    # SPESIFIKASI: mencetak game dalam tokogame dalam urutan yang diinginkan
    # KAMUS LOKAL
        # skema : string
        # N : integer
        # ascending : boolean
        # kolom : integer
        # sortpass, i_min, i, ind_min_value, i_value : integer
        # common.iterLength(iterable : string or array) -> integer
        # common.remove_thousands(numstr : string) -> string
        # common.alignTable(arr: array of array) -> array of array
    # ALGORITMA
    skema = input('Skema sorting: ')
    print()
    if skema == 'tahun+' or skema == 'tahun-' or skema == 'harga+' or skema == 'harga-' or skema =='':
        N = common.iterLength(tokogame)  # jumlah baris tokogame
        
        if N > 1:   # melakukan sort terurut membesar apabila isi array lebih dari 1 baris
            if skema == '':     # kolom yang ditinjau adalah ID, urutan pencetakan hasil membesar
                ascending = True
                kolom = 0

            else:               # pengurutan berdasarkan tahun atau harga
                if skema[5] == '+':     # menentukan urutan pencetakan hasil akhir
                    ascending = True
                else:
                    ascending = False
                
                if skema == 'tahun+' or skema == 'tahun-':      # kolom yang ditinjau adalah tahun
                    kolom = 4
                else:                                           # kolom yang ditinjau adalah harga
                    kolom = 2
            
            for sortpass in range(0,N):     # selection sort : terurut membesar
                i_min = sortpass
                for i in range((sortpass+1), N):
                    # penetapan pembanding
                    if kolom == 0:
                        ind_min_value = int(tokogame[i_min][kolom][4] + tokogame[i_min][kolom][5] + tokogame[i_min][kolom][6])
                        i_value = int(tokogame[i][kolom][4] + tokogame[i][kolom][5] + tokogame[i][kolom][6])
                    else:
                        ind_min_value = int(common.remove_thousands(tokogame[i_min][kolom]))
                        i_value = int(common.remove_thousands(tokogame[i][kolom]))
                    
                    if i_value < ind_min_value:
                        i_min = i
                
                temp = tokogame[i_min]
                tokogame[i_min] = tokogame[sortpass]
                tokogame[sortpass] = temp
        

        # proses mencetak hasil sort
        tokogame = common.alignTable(tokogame)  # menyejajarkan spasi pada array (tabel)
        if ascending:   # mencetak tokogame dengan urutan sama; terurut membesar
            for i in range(N):
                print(f'{i+1}. ' + common.arr_to_str(tokogame[i],' | '))
        else:   # mencetak tokogame dengan urutan terbalik; terurut mengecil
            for i in range(N-1, -1, -1):
                print(f'{N-i}. ' + common.arr_to_str(tokogame[i],' | '))

                
    else:
        print('Skema sorting tidak valid!')
