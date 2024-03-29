'''
MODUL F14-Help
Spesifikasi : Menampilkan fitur program ke layar sebagai bantuan user
I.S. : Membaca role
F.S. : Menampilkan bantuan fitur program ke layar
Desainer dan coder : 16521199
'''

def Help(user_role): 
    if user_role=='':  #blm log in
        print("===========HELP===========")
        print("1. login - Untuk melakukan login ke dalam sistem")
        print("2. help - Untuk memberikan panduan penggunaan sistem")
        print("3. exit - Untuk keluar dari aplikasi")
        print("4. kerangajaib - Untuk bermain bersama kerang ajaib")
        print("5. tictactoe - Untuk bermain tic-tac-toe")
    else: #sudah log in
        if user_role=='Admin': #admin
            print("===========HELP===========")
            print("1. register - Untuk melakukan registrasi user baru" )
            print("2. login - Untuk melakukan login ke dalam sistem")
            print("3. tambah_game - Untuk menambah game yang dijual pada toko")
            print("4. ubah_game - Untuk mengubah game pada toko game")
            print("5. ubah_stok - Untuk mengubah stok sebuah game pada toko")
            print("6. list_game_toko - Untuk melihat list game yang dijual pada toko")
            print("7. search_game_at_store - Untuk mencari game yang terdapat di toko")
            print("8. topup - Untuk menambahkan saldo kepada user")
            print("9. help - Untuk memberikan panduan penggunaan sistem")
            print("10. save - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan")
            print("11. exit - Untuk keluar dari aplikasi")
            print("12. kerangajaib - Untuk bermain bersama kerang ajaib")
            print("13. tictactoe - Untuk bermain tic-tac-toe")
        else: #user
            print("===========HELP===========")
            print("1. login - Untuk melakukan login ke dalam sistem ")
            print("2. list_game_toko - Untuk melihat list game yang dijual pada toko")
            print("3. buy_game - Untuk membeli game yang dijual")
            print("4. list_game - Untuk memberikan daftar game yang dimiliki user")
            print("5. search_my_game - Untuk mencari game yang dimiliki user")
            print("6. search_game_at_store - Untuk mencari game yang terdapat di toko")     
            print("7. riwayat - Untuk melihat riwayat pembelian game")
            print("8. help - Untuk memberikan panduan penggunaan sistem")    
            print("9. save - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan")
            print("10. exit - Untuk keluar dari aplikasi")
            print("11. kerangajaib - Untuk bermain bersama kerang ajaib")
            print("12. tictactoe - Untuk bermain tic-tac-toe")
