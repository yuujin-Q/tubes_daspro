# tubes_daspro
Tubes Daspro-K01 Kelompok 3

Anggota:

--172 Arleen Chrysantha Gunardi
--199 Jazila Faza Aliyya Nurfauzi
--262 Fawwazti Rasendria
--316 Eugene Yap Jin Quan



Deskripsi Persoalan:
BNMO adalah sebuah robot game milik Indra dan Doni yang memiliki sistem inventarisasi dan toko game yang baik.
Pada suatu saat, BNMO rusak akibat dibanting Indra. 
Apakah kita bisa membantu Doni memperbaiki BNMO (dengan memrogram ulang BNMO)?.



Spesifikasi Program:

F01 - Dekomposisi, Abstraksi dan Generalisasi Pola dengan Modular Programming	
F02 - Register	
  {akses: role admin
  fungsi: mendaftarkan pengguna baru (role user)
  parameter: nama, username, password
  spesifikasi username: unik, memiliki role user, mengandung alphanumeric, underscore '_', dash '-'}

F03 - Login	
  {akses: role user dan role admin
  fungsi: login ke aplikasi
  parameter: username, password}
  
F04 - Menambah Game ke Toko Game	
  {akses: admin
  fungsi: melakukan penambahan informasi game ke file csv, melakukan validasi terlebih dahulu}
  
F05 - Mengubah Game pada Toko Game	
  {akses: admin
  fungsi: mengubah data game (tidak mengubah stock)}
  
F06 - Mengubah Stok Game di Toko	
  {akses: admin
  fungsi: mengubah stok game (validasi tidak negatif)}
  
F07 - Listing Game di Toko Berdasarkan ID, Tahun Rilis dan Harga	
  {akses: user dan admin
  fungsi: menampilkan data game dengan sorting}
  
F08 - Membeli dan Menjual Game	
  {akses: user
  fungsi: membeli game (1 game sebanyak 1 kali pada 1 user)}
  
F09 - Melihat Game yang dimiliki	
  {akses: user
  fungsi: melihat game yg dimiliki}
  
F10 - Mencari Game yang dimiliki dari ID dan tahun rilis	
  {akses: user
  fungsi: search inventory game berdasarkan ID dan tahun rilis}
  
F11 - Mencari Game di Toko dari ID, Nama Game, Harga, Kategori dan Tahun Rilis	
  {akses: admin, user
  fungsi: search toko game berdasarkan ID, nama, harga, kategori, dan tahun rilis}
  
F12 - Top Up Saldo	
  {akses: admin
  fungsi: mengisi saldo (saldo boleh minus, tetapi input saldo tidak negatif)}
  
F13 - Melihat Riwayat Pembelian	
  {akses: user
  fungsi : riwayat pembelanjaan}

F14 - Help	
  {akses: admin, user
  fungsi: mencetak panduan sistem}
  
F15 - Load	
  {fungsi: loading data ke sistem (otomatis)}
  
F16 - Save	
  {akses: admin, user
  fungsi: menyimpan perubahan data (contoh pembelian atau penjualan) ke file csv.}
  
F17 - Exit
  {fungsi: keluar dari sistem}
