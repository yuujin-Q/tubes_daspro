'''
MODUL F04-Menambah Game ke Toko Game
Spesifikasi: Menambah game ke toko melalui pengisian informasi game.
I.S. : array game terdefinisi
F.S. : game mempunyai baris baru yang berisi data baru
Desainer dan coder : 16521262, 16521316
'''
import f_common as common


def tambah_game(game):
    # SPESIFIKASI: menambahkan game baru pada array data
    # KAMUS LOKAL
        # nama_game, kategori, tahun_rilis, harga, stok_awal, id: string
        # last_id : integer
        # common.iterLength(iterable : string or array) -> integer
    # ALGORITMA
    while True:
        # input dari user
        nama_game = input('Masukkan nama game: ')
        kategori = input('Masukkan kategori: ')
        tahun_rilis = input('Masukkan tahun rilis: ')
        harga = input('Masukkan harga: ')
        stok_awal = input('Masukkan stok awal: ')
        
        # cek apakah terdapat informasi yang belum di-input
        if nama_game == '' or kategori =='' or tahun_rilis =='' or harga=='' or stok_awal=='':  #jika ada input kosong
            print("\nMohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        else:       # semua input terisi
            break
    
    # membuat game id
    last_id = common.iterLength(game)
    if last_id < 100 :
        id = 'GAME0' + str(last_id)
    else:
        id = 'GAME' + str(last_id)
    
    game += [[id, nama_game, kategori, tahun_rilis, harga, stok_awal]]      # menambahkan baris baru pada game
    return game     # return game