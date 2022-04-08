#fungsi untuk mencari game di toko oleh user dan admin
def search_game_at_store():
    id_game = input("Masukkan ID game: ")
    nama_game = input("Masukkan Nama game: ")
    harga = input("Masukkan Harga Game: ")
    kategori = input("Masukkan Kategori Game: ")
    tahun_rilis = input("Masukkan Tahun Rilis Game: ")
    print("Dafar game pada toko yang memenuhi kriteria: ")
    