#fungsi top up oleh admin
def topup():
    username = input("Masukkan username: ")
    saldo = input("Masukkan saldo: ")
    #masukan bener
    print("Top up berhasil. Saldo", username, "bertambah menjadi", saldo)
    #saldo < 0
    print("Masukan tidak valid")
    #user g ditemukan
    print("Username ", username, " tidak ditemukan. ")