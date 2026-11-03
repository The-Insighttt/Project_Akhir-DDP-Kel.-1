# Sistem Pemesanan Layanan IT Support

Proyek Akhir Praktikum Dasar-Dasar Pemrograman
Program Studi Sistem Informasi, Fakultas Teknik, Universitas Mulawarman (2026)
Kelompok 1 (The Insight)

## 1. Judul / Tema

Sistem Pemesanan Layanan IT Support adalah aplikasi berbasis terminal (CLI) yang dibuat dengan Python. Tema proyeknya adalah digitalisasi pemesanan jasa IT Support, seperti instalasi komputer, maintenance, konsultasi IT, dan instalasi software, dengan sistem saldo dan pencatatan transaksi otomatis.

## 2. Anggota & Peran

| No | Nama | NIM | Peran |
|----|------|-----|-------|
| 1 | Ahmad Aimar Refaldi Ramang | 2609116056 | (isi peran) |
| 2 | Muhammad Sholahuddin Sanjaya | 2609116048 | (isi peran) |
| 3 | Efraim Juniar Tonda Kala' | 2609116064 | (isi peran) |
| 4 | Graceilla Tifunny Glory Hutagalung | 2609116079 | (isi peran) |

Asisten Laboratorium: Muhammad Davi Aditya Pratama (2509116070) dan Hanif Amelia Putri (2509116075)

## 3. Deskripsi & Tujuan

### Deskripsi
Pemesanan layanan IT Support masih sering dilakukan manual lewat pesan singkat, telepon, atau datang langsung. Akibatnya pencatatan tidak teratur, pesanan bisa terlewat, dan tarif kurang transparan. Program ini menyatukan proses tersebut dalam satu sistem. Customer (user) dapat melihat layanan beserta harga dan kuota, mengisi saldo, lalu memesan layanan. Admin mengelola daftar layanan, memantau seluruh transaksi, dan melihat laporan pendapatan. Program cocok dipakai oleh unit layanan komputer di kampus, laboratorium, kantor, atau toko servis perangkat.

### Tujuan
1. Membangun registrasi dan login yang membedakan hak akses Admin dan User.
2. Menampilkan daftar layanan IT Support beserta harga dan kuota secara rapi.
3. Menyediakan fitur CRUD layanan bagi Admin.
4. Memproses pemesanan oleh User (validasi kuota dan saldo, invoice) dan mencatatnya otomatis.
5. Membantu Admin memantau seluruh transaksi lewat riwayat dan laporan ringkas.

## 4. Flowchart

<img width="833" height="861" alt="image" src="https://github.com/user-attachments/assets/ee7f4507-6d10-45c9-a74f-cca6a5f3294c" />

**Menu Utama:** Program dimulai dari menu utama dengan tiga pilihan: Registrasi, Login, dan Keluar. Saat registrasi, sistem memeriksa format dan keunikan username sebelum menyimpan akun ke JSON. Login dibatasi 3 kali percobaan. Jika berhasil, sistem memeriksa role: admin menuju Menu Admin, selain itu menuju Menu User.

<img width="833" height="622" alt="image" src="https://github.com/user-attachments/assets/ed60c79f-bca6-402d-a802-d871742295dc" />

**Menu Admin:** Admin dapat melihat, menambah, mengubah, dan menghapus layanan (hapus memerlukan konfirmasi y/n), melihat laporan, dan melihat seluruh riwayat transaksi. Setiap proses kembali ke Menu Admin sampai admin memilih Logout.

<img width="833" height="587" alt="image" src="https://github.com/user-attachments/assets/7c5d7566-97f8-4c1b-9798-43324add9cd8" />

**Menu User:** User dapat melihat layanan, memesan, top up saldo, melihat riwayat, dan melihat saldo. Pada pemesanan, sistem memeriksa ID layanan, kuota, lalu saldo. Jika semua cukup, saldo dan kuota dikurangi, transaksi disimpan ke CSV, dan invoice dicetak.

## 5. Daftar Fitur per Role

### Umum (sebelum login)
- Registrasi: username minimal 4 karakter alfanumerik dan unik, password minimal 6 karakter, role otomatis user dengan saldo awal Rp0.
- Login: password tersamarkan, maksimal 3 kali percobaan salah.
- Keluar: mengakhiri program.

### User
1. Lihat Layanan: menampilkan daftar layanan (ID, jenis, harga, kuota).
2. Pesan Layanan: memilih layanan dan jumlah, validasi kuota dan saldo, invoice sementara, konfirmasi, lalu invoice final.
3. Top Up: menambah saldo (harus angka dan lebih dari 0).
4. Riwayat Transaksi: riwayat pesanan milik user sendiri.
5. Lihat Saldo: menampilkan saldo saat ini.
6. Logout.

### Admin
1. Lihat Layanan.
2. Tambah Layanan: ID unik, jenis, harga dan kuota lebih dari 0.
3. Ubah Layanan: mengubah jenis, harga, dan kuota berdasarkan ID.
4. Hapus Layanan: dengan konfirmasi y/n.
5. Laporan Admin: total pendapatan, jumlah transaksi, layanan terlaris, jumlah terjual.
6. Riwayat Semua Transaksi: transaksi seluruh user beserta waktu.
7. Logout.

## 6. Screenshot Output & Penjelasan

**Menu Utama:** tampilan awal program dengan pilihan 1. Registrasi, 2. Login, 3. Keluar.

**Registrasi:** user mengisi username, nama, dan password (tersamarkan). Jika valid, akun disimpan ke data_pengguna.json dan muncul pesan "Registrasi berhasil!".

**Login:** login pertama gagal sehingga sisa percobaan menjadi 2. Percobaan kedua berhasil dan user masuk ke menu sesuai role.

**Menu User:** menu utama user berisi 6 pilihan.

**Lihat Layanan (User):** daftar layanan beserta harga dan sisa kuota dalam bentuk tabel.

**Pesan Layanan:** user memilih L03 dengan jumlah 3. Sistem menampilkan invoice sementara (total Rp90.000, saldo Rp100.000) dan meminta konfirmasi. Setelah "y", saldo dan kuota berkurang, transaksi tersimpan ke CSV, dan invoice final dicetak lengkap dengan tanggal dan waktu.

**Top Up Saldo:** user mengisi nominal Rp20.000. Saldo bertambah dan langsung tersimpan ke file JSON.

**Riwayat Transaksi (User):** menampilkan transaksi milik user yang login: kode transaksi, ID layanan, jumlah, dan total.

**Lihat Saldo:** menampilkan saldo terkini milik user.

**Logout (User):** user keluar dari akun dan kembali ke menu utama.

**Menu Admin:** menu khusus admin berisi 7 pilihan.

**Lihat Layanan (Admin):** admin melihat seluruh layanan beserta harga dan kuota.

**Tambah Layanan:** admin menambahkan layanan baru (L04 - Instalasi Hardware, Rp60.000, kuota 10), lalu data tersimpan ke data_layanan.json.

**Ubah Layanan:** admin mengubah layanan L04 menjadi "Instalasi Software" dengan harga dan kuota baru.

**Hapus Layanan:** admin menghapus layanan L04 setelah konfirmasi.

**Laporan Admin:** ringkasan total pendapatan, jumlah transaksi, layanan terlaris, dan jumlah terjual, dihitung dari data_transaksi.csv.

**Riwayat Semua Transaksi:** seluruh transaksi dari semua user lengkap dengan waktu transaksi.

**Logout (Admin):** admin keluar dari akun dan kembali ke menu utama.
