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
| 2 | Muhammad Sholahuddin Sanjaya | 2609116048 | Konsep Program, Logika Program, Flowchart, Pengecekan Alur Program |
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

<img width="1559" height="1612" alt="Flowchart Project Akhir-MENU UTAMA drawio" src="https://github.com/user-attachments/assets/30365033-22ce-45a1-9d06-ec4ea2800a40" />

**Menu Utama:** Program dimulai dari START, lalu menampilkan Menu Utama dengan tiga pilihan, yaitu 1. Registrasi, 2. Login, dan 3. Keluar. Program kemudian memeriksa pilihan pengguna.
1.	Registrasi (Pilihan 1)
a.	Pengguna memasukkan username dan password.
b.	Sistem memeriksa apakah format input valid. Jika tidak valid, sistem menampilkan pesan error dan pengguna kembali diminta memasukkan username.
c.	Jika format valid, sistem memeriksa apakah username sudah ada di data. Jika sudah ada, sistem menampilkan pesan error dan pengguna mengulang dari input username.
d.	Jika username belum terdaftar, sistem membuat akun baru dan menyimpannya ke file JSON.
e.	Setelah data tersimpan, sistem menampilkan pesan "Registrasi Berhasil", lalu kembali ke Menu Utama.
3.	Login (Pilihan 2)
a.	Pengguna memasukkan username dan password.
b.	Sistem mencocokkan keduanya dengan data yang tersimpan.
c.	Jika sesuai, sistem menampilkan pesan login berhasil, lalu memeriksa role pengguna. Jika role adalah admin, alur menuju konektor B (Menu Admin). Jika bukan admin, alur menuju konektor C (Menu User).
d.	Jika tidak sesuai, sistem menghitung percobaan login yang gagal dan menampilkan pesan gagal. Kemudian sistem mengecek apakah percobaan sudah mencapai batas 3 kali. Jika belum, pengguna diminta memasukkan data kembali. Jika sudah, sistem menampilkan pesan bahwa login diblokir dan kembali ke Menu Utama.
5.	Keluar (Pilihan 3): program menuju END dan berhenti.
6.	Input selain 1, 2, dan 3: sistem menampilkan pesan "Input tidak valid" lalu kembali ke Menu Utama.

<img width="2052" height="1532" alt="Flowchart Project Akhir-ADMIN drawio" src="https://github.com/user-attachments/assets/53a93d5c-f9ea-4bc4-81e6-014fd974f266" />

**Menu Admin:** Setelah admin login, sistem menampilkan menu: 1. Tampilkan Layanan, 2. Tambah Layanan, 3. Ubah Layanan, 4. Hapus Layanan, 5. Lihat Riwayat Transaksi, 6. Laporan, dan 7. Log Out.

1.	Tampilkan Layanan (Pilihan 1): sistem mengambil data daftar layanan dari database JSON, lalu menampilkan seluruh layanan yang tersedia.
2.	Tambah Layanan (Pilihan 2): admin memasukkan ID layanan baru, jenis layanan, harga jasa, dan kuota pegawai yang bisa melakukan layanan tersebut. Layanan baru disimpan ke database, lalu sistem menampilkan pesan "Layanan Baru telah Ditambahkan".
3.	Ubah Layanan (Pilihan 3): sistem menampilkan daftar layanan, lalu admin memilih ID layanan yang ingin diubah. Admin dapat mengubah jenis layanan, harga jasa, dan kuota pegawai. Data lama diperbarui di database, lalu sistem menampilkan pesan "Data layanan Telah Diperbarui".
4.	Hapus Layanan (Pilihan 4): sistem menampilkan daftar layanan, lalu admin memilih ID layanan yang ingin dihapus. Sistem meminta konfirmasi (y/n). Jika dikonfirmasi, data diperbarui dengan menghapus layanan tersebut, lalu sistem menampilkan pesan "Data telah Dihapus".
5.	Lihat Riwayat Transaksi (Pilihan 5): sistem mengambil data riwayat transaksi dari database CSV, lalu menampilkan seluruh riwayat transaksi.
6.	Laporan (Pilihan 6): sistem mengambil data dari database CSV, lalu menampilkan laporan ringkas.
7.	Log Out (Pilihan 7): admin keluar dari akun dan alur kembali ke Menu Utama melalui konektor A.
8.	Input selain 1 sampai 7: sistem menampilkan "Input Tidak Valid" dan kembali ke Menu Admin.
Setiap proses di atas berakhir dengan kembali ke tampilan Menu Admin, sehingga admin dapat memilih fitur lain.

<img width="2512" height="1772" alt="Flowchart Project Akhir-USER drawio" src="https://github.com/user-attachments/assets/27cbba22-3571-4b5c-928f-5d95f64b0bfa" />

**Menu User:** Setelah user login, sistem menampilkan menu: 1. Lihat Layanan, 2. Pesan, 3. Top Up, 4. Lihat Riwayat, 5. Lihat Saldo, dan 6. Log Out.
1.	Lihat Layanan (Pilihan 1): sistem mengambil data layanan dari database JSON dan menampilkannya kepada user.
2.	Pesan (Pilihan 2)
a.	Sistem menampilkan daftar layanan, lalu user memasukkan ID layanan dan jumlah pesanan.
b.	Sistem memvalidasi ID dan input. Jika tidak valid, muncul pesan error dan user mengulang input.
c.	Jika valid, sistem memeriksa apakah kuota layanan mencukupi. Jika tidak, muncul pesan error dan user mengulang input.
d.	Jika mencukupi, sistem menghitung total = harga * jumlah.
e.	Sistem memeriksa apakah saldo user cukup. Jika tidak, sistem menampilkan pesan "Saldo tidak cukup, silakan top up". Jika cukup, saldo dikurangi total (saldo = saldo - total) dan kuota layanan dikurangi jumlah pesanan (kuota = kuota - jumlah).
f.	Sistem membuat kode transaksi, menyimpan pesanan ke database CSV, lalu menampilkan pesan "Layanan telah Disimpan".
3.	Top Up (Pilihan 3)
a.	User memasukkan nominal top up.
b.	Sistem memeriksa apakah input berupa angka. Jika bukan, muncul pesan error dan user mengulang input.
c.	Sistem memeriksa apakah nominal lebih dari 0. Jika tidak, muncul pesan error dan user mengulang input.
d.	Jika memenuhi, saldo diperbarui (saldo = saldo + nominal) dan disimpan ke database JSON.
e.	Sistem menampilkan saldo terbaru.
4.	Lihat Riwayat (Pilihan 4): sistem mengambil data riwayat transaksi dari database CSV, lalu menampilkan riwayat transaksi milik user itu sendiri.
5.	Lihat Saldo (Pilihan 5): sistem mengambil data saldo user, lalu menampilkan saldo saat ini.
6.	Log Out (Pilihan 6): user keluar dari akun dan alur kembali ke Menu Utama melalui konektor A.
7.	Input selain 1 sampai 6: sistem menampilkan "Input Tidak Valid" dan kembali ke Menu User.

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
