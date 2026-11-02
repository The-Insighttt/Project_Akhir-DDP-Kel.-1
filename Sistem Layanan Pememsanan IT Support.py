import json
import csv
import os
import time
import pwinput
from prettytable import PrettyTable

akun_file = "data_pengguna.json"
layanan_file = "data_layanan.json"
transaksi_file = "data_transaksi.csv"


os.system("cls" if os.name == "nt" else "clear")

def load_users():
    if os.path.exists(akun_file):
        with open(akun_file, "r") as file:
            return json.load(file)
    return {}

def save_users():
    with open(akun_file, "w") as file:
        json.dump(data_pengguna, file, indent=4)


data_pengguna = load_users()


def load_layanan():
    if os.path.exists(layanan_file):
        with open(layanan_file, "r") as file:
            return json.load(file)
    return {}


def save_layanan():
    with open(layanan_file, "w") as file:
        json.dump(data_layanan, file, indent=4)

data_layanan = load_layanan()


def load_transaksi():
    transaksi = []

    if not os.path.exists("data_transaksi.csv"):
        return transaksi

    with open("data_transaksi.csv", "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            waktu = (
                row.get("waktu")
                or row.get("Waktu")
                or row.get("tanggal_waktu")
                or row.get("timestamp")
                or "-"
            )

            transaksi.append({
                "kode_transaksi": row.get("kode_transaksi", "-"),
                "username": row.get("username", "-"),
                "id_layanan": row.get("id_layanan", "-"),
                "jumlah": row.get("jumlah", "-"),
                "total": row.get("total", "-"),
                "waktu": waktu
            })

    return transaksi

data_transaksi = load_transaksi()


def input_angka_ulang(prompt, minimum=None, maksimum=None, pesan_min=None, pesan_max=None):
    """Mengulang input sampai angka valid; Ctrl+C hanya memberi peringatan."""
    while True:
        try:
            nilai = int(input(prompt))
            if minimum is not None and nilai < minimum:
                print(pesan_min or f"Nilai minimal adalah {minimum}.")
                continue
            if maksimum is not None and nilai > maksimum:
                print(pesan_max or f"Nilai maksimal adalah {maksimum}.")
                continue
            return nilai
        except ValueError:
            print("Input harus berupa angka! Silakan masukkan lagi.")
        except KeyboardInterrupt:
            print("\nPeringatan: Ctrl+C terdeteksi. Silakan masukkan input lagi.")
            continue




def registrasi():
    print("\n===== REGISTRASI =====")
    try:
        while True:
            try:
                username = input("Username : ").strip()
            except KeyboardInterrupt:
                print("\nPeringatan: Ctrl+C terdeteksi. Masukkan username lagi.")
                continue
            if len(username) < 4 or not username.isalnum():
                print("Username minimal 4 karakter dan tanpa spasi! Coba lagi.")
                continue
            if username in data_pengguna:
                print("Username sudah digunakan! Masukkan username lain.")
                continue
            break

        while True:
            try:
                nama = input("Nama : ").strip()
            except KeyboardInterrupt:
                print("\nPeringatan: Ctrl+C terdeteksi. Masukkan nama lagi.")
                continue
            if not nama:
                print("Nama tidak boleh kosong! Coba lagi.")
                continue
            break

        while True:
            try:
                password = pwinput.pwinput(prompt="Password : ", mask="*")
            except KeyboardInterrupt:
                print("\nPeringatan: Ctrl+C terdeteksi. Masukkan password lagi.")
                continue
            if len(password) < 6:
                print("Password minimal 6 karakter! Coba lagi.")
                continue
            break

        data_pengguna[username] = {
            "nama": nama,
            "password": password,
            "role": "user",
            "saldo": 0
        }
        save_users()
        print("Registrasi berhasil!")

    except EOFError:
        print("\nPeringatan: Input berakhir (EOF). Registrasi dibatalkan.")
    except ValueError as e:
        print("Input tidak valid:", e)



def login():
    print("\n===== LOGIN =====")
    percobaan = 0

    while percobaan < 3:
        try:
            try:
                username = input("Username : ").strip()
                password = pwinput.pwinput(prompt="Password : ", mask="*")
            except KeyboardInterrupt:
                print("\nPeringatan: Ctrl+C terdeteksi. Silakan masukkan username dan password lagi.")
                continue

            if (
                username in data_pengguna
                and data_pengguna[username]["password"] == password
            ):
                print("Login berhasil!")
                if data_pengguna[username]["role"] == "admin":
                    menu_admin()
                else:
                    menu_user(username)
                return

            percobaan += 1
            print("Username atau password salah!")
            print("Sisa percobaan:", 3 - percobaan)
        except EOFError:
            print("\nPeringatan: Input berakhir (EOF). Login dibatalkan.")
            return

    print("Batas login tercapai. Silakan coba login kembali nanti.")


def lihat_layanan():
    print("\n===== DAFTAR LAYANAN =====")

    if not data_layanan:
        print("Belum ada layanan.")
        return

    tabel = PrettyTable()

    tabel.field_names = [
        "ID Layanan",
        "Jenis Layanan",
        "Harga",
        "Kuota"
    ]

    for id_layanan, layanan in data_layanan.items():
        tabel.add_row([
            id_layanan,
            layanan["jenis"],
            layanan["harga"],
            layanan["kuota"]
        ])

    print(tabel)



def tambah_layanan():
    lihat_layanan()
    print("\n===== TAMBAH LAYANAN =====")
    try:
        while True:
            try:
                id_layanan = input("ID Layanan : ").strip()
            except KeyboardInterrupt:
                print("\nPeringatan: Ctrl+C terdeteksi. Masukkan ID layanan lagi.")
                continue
            if not id_layanan:
                print("ID layanan tidak boleh kosong!")
                continue
            if id_layanan in data_layanan:
                print("ID layanan sudah digunakan! Masukkan ID lain.")
                continue
            break

        while True:
            try:
                jenis = input("Jenis Layanan : ").strip()
            except KeyboardInterrupt:
                print("\nPeringatan: Ctrl+C terdeteksi. Masukkan jenis layanan lagi.")
                continue
            if not jenis:
                print("Jenis layanan tidak boleh kosong!")
                continue
            break

        harga = input_angka_ulang(
            "Harga : ", minimum=1,
            pesan_min="Harga harus lebih dari 0!"
        )
        kuota = input_angka_ulang(
            "Kuota : ", minimum=1,
            pesan_min="Kuota harus lebih dari 0!"
        )

        data_layanan[id_layanan] = {
            "jenis": jenis,
            "harga": harga,
            "kuota": kuota
        }
        save_layanan()
        print("Layanan berhasil ditambahkan!")
    except EOFError:
        print("\nPeringatan: Input berakhir (EOF). Penambahan layanan dibatalkan.")


def riwayat_semua_transaksi():
    global data_transaksi

    print("\n===== SEMUA RIWAYAT TRANSAKSI =====")

    data_transaksi = load_transaksi()

    if not data_transaksi:
        print("Belum ada transaksi.")
        return

    tabel = PrettyTable()
    tabel.field_names = [
        "Kode Transaksi",
        "Username",
        "ID Layanan",
        "Jumlah",
        "Total",
        "Waktu"
    ]

    for trx in data_transaksi:
        tabel.add_row([
            trx.get("kode_transaksi", "-"),
            trx.get("username", "-"),
            trx.get("id_layanan", "-"),
            trx.get("jumlah", "-"),
            trx.get("total", "-"),
            trx.get("waktu", "-")
        ])

    print(tabel)



def laporan_admin():
    print("\n===== LAPORAN RINGKAS ADMIN =====")

    if not data_transaksi:
        print("Belum ada transaksi.")
        return

    total_pendapatan = 0
    jumlah_transaksi = len(data_transaksi)
    jumlah_layanan = {}

    for trx in data_transaksi:
        total_pendapatan += int(trx["total"])

        id_layanan = trx["id_layanan"]
        jumlah = int(trx["jumlah"])

        if id_layanan in jumlah_layanan:
            jumlah_layanan[id_layanan] += jumlah
        else:
            jumlah_layanan[id_layanan] = jumlah

    id_terlaris = max(
        jumlah_layanan,
        key=jumlah_layanan.get
    )

    jumlah_terlaris = jumlah_layanan[id_terlaris]

    layanan = data_layanan.get(id_terlaris)

    if layanan:
        nama_layanan = layanan["jenis"]
    else:
        nama_layanan = id_terlaris

    tabel = PrettyTable()
    tabel.field_names = ["Keterangan", "Hasil"]

    tabel.add_row([
        "Total Pendapatan",
        "Rp" + f"{total_pendapatan:,}".replace(",", ".")
    ])

    tabel.add_row([
        "Jumlah Transaksi",
        jumlah_transaksi
    ])

    tabel.add_row([
        "Layanan Terlaris",
        nama_layanan
    ])

    tabel.add_row([
        "Jumlah Terjual",
        jumlah_terlaris
    ])

    print(tabel)



def ubah_layanan():
    lihat_layanan()
    print("\n===== UBAH LAYANAN =====")
    try:
        while True:
            try:
                id_layanan = input("ID Layanan : ").strip()
            except KeyboardInterrupt:
                print("\nPeringatan: Ctrl+C terdeteksi. Masukkan ID layanan lagi.")
                continue
            if id_layanan not in data_layanan:
                print("Layanan tidak ditemukan! Masukkan ID yang benar.")
                continue
            break

        while True:
            try:
                jenis = input("Jenis Layanan baru : ").strip()
            except KeyboardInterrupt:
                print("\nPeringatan: Ctrl+C terdeteksi. Masukkan jenis layanan lagi.")
                continue
            if not jenis:
                print("Jenis layanan tidak boleh kosong!")
                continue
            break

        harga = input_angka_ulang(
            "Harga baru : ", minimum=1,
            pesan_min="Harga harus lebih dari 0!"
        )
        kuota = input_angka_ulang(
            "Kuota baru : ", minimum=1,
            pesan_min="Kuota harus lebih dari 0!"
        )

        data_layanan[id_layanan]["jenis"] = jenis
        data_layanan[id_layanan]["harga"] = harga
        data_layanan[id_layanan]["kuota"] = kuota
        save_layanan()
        print("Layanan berhasil diubah!")
    except EOFError:
        print("\nPeringatan: Input berakhir (EOF). Perubahan dibatalkan.")



def hapus_layanan():
    lihat_layanan()
    print("\n===== HAPUS LAYANAN =====")
    if not data_layanan:
        return

    while True:
        try:
            id_layanan = input("ID Layanan : ").strip()
        except KeyboardInterrupt:
            print("\nPeringatan: Ctrl+C terdeteksi. Masukkan ID layanan lagi.")
            continue
        if id_layanan not in data_layanan:
            print("Layanan tidak ditemukan! Masukkan ID yang benar.")
            continue
        break

    while True:
        try:
            konfirmasi = input("Yakin hapus layanan ini? (y/n): ").strip().lower()
        except KeyboardInterrupt:
            print("\nPeringatan: Ctrl+C terdeteksi. Masukkan y atau n lagi.")
            continue
        if konfirmasi not in ("y", "n"):
            print("Input harus y atau n. Coba lagi.")
            continue
        break

    if konfirmasi == "n":
        print("Penghapusan dibatalkan.")
        return

    del data_layanan[id_layanan]
    save_layanan()
    print("Layanan berhasil dihapus!")



def menu_admin():
    while True:
        print("\n===== MENU ADMIN =====")
        print("1. Lihat Layanan")
        print("2. Tambah Layanan")
        print("3. Ubah Layanan")
        print("4. Hapus Layanan")
        print("5. Laporan Admin")
        print("6. Riwayat Semua Transaksi")
        print("7. Logout")

        try:
            pilihan = input_angka_ulang(
                "Pilih : ", minimum=1, maksimum=7,
                pesan_min="Pilihan tidak tersedia! Masukkan angka 1-7.",
                pesan_max="Pilihan tidak tersedia! Masukkan angka 1-7."
            )
        except EOFError:
            print("\nPeringatan: Input berakhir (EOF).")
            continue

        if pilihan == 1:
            lihat_layanan()
        elif pilihan == 2:
            tambah_layanan()
        elif pilihan == 3:
            ubah_layanan()
        elif pilihan == 4:
            hapus_layanan()
        elif pilihan == 5:
            laporan_admin()
        elif pilihan == 6:
            riwayat_semua_transaksi()
        elif pilihan == 7:
            print("Logout berhasil!")
            break



def top_up(username):
    print("\n===== TOP UP SALDO =====")
    try:
        nominal = input_angka_ulang(
            "Nominal Top Up : Rp", minimum=1,
            pesan_min="Nominal harus lebih dari 0!"
        )
        data_pengguna[username]["saldo"] += nominal
        save_users()
        print("Top up berhasil!")
        print("Nominal Top Up : Rp" + f"{nominal:,}".replace(",", "."))
        print("Saldo Sekarang : Rp" + f"{data_pengguna[username]['saldo']:,}".replace(",", "."))
    except EOFError:
        print("\nPeringatan: Input berakhir (EOF). Top up dibatalkan.")


def cetak_invoice(transaksi):
    print("\n===== INVOICE =====")

    username = transaksi["username"]
    id_layanan = transaksi["id_layanan"]

    layanan = data_layanan.get(id_layanan)

    tabel = PrettyTable()
    tabel.field_names = ["Keterangan", "Detail"]

    waktu = time.strftime("%d-%m-%Y %H:%M:%S")

    tabel.add_row([
    "Tanggal & Waktu",
    waktu
])

    tabel.add_row([
        "Kode Transaksi",
        transaksi["kode_transaksi"]
    ])

    tabel.add_row([
        "Username",
        username
    ])

    if layanan:
        tabel.add_row([
            "Jenis Layanan",
            layanan["jenis"]
        ])

        tabel.add_row([
            "Harga",
            f"Rp{layanan['harga']:,}".replace(",", ".")
        ])

    tabel.add_row([
        "ID Layanan",
        id_layanan
    ])

    tabel.add_row([
        "Jumlah",
        transaksi["jumlah"]
    ])

    tabel.add_row([
        "Total Bayar",
        f"Rp{int(transaksi['total']):,}".replace(",", ".")
    ])

    print(tabel)
    print("Terima kasih telah memesan!")




def pesan_layanan(username):
    print("\n===== PESAN LAYANAN =====")
    if not data_layanan:
        print("Belum ada layanan.")
        return

    tabel = PrettyTable()
    tabel.field_names = ["ID Layanan", "Jenis Layanan", "Harga", "Kuota"]
    for id_layanan, layanan in data_layanan.items():
        tabel.add_row([
            id_layanan, layanan["jenis"],
            f"Rp{layanan['harga']:,}".replace(",", "."),
            layanan["kuota"]
        ])
    print(tabel)

    try:
        while True:
            try:
                id_layanan = input("ID Layanan : ").strip()
            except KeyboardInterrupt:
                print("\nPeringatan: Ctrl+C terdeteksi. Masukkan ID layanan lagi.")
                continue
            if id_layanan not in data_layanan:
                print("Layanan tidak ditemukan! Masukkan ID yang benar.")
                continue
            break

        layanan = data_layanan[id_layanan]
        jumlah = input_angka_ulang(
            "Jumlah : ", minimum=1,
            pesan_min="Jumlah harus lebih dari 0!"
        )

        while jumlah > layanan["kuota"]:
            print(f"Kuota tidak mencukupi! Kuota tersedia: {layanan['kuota']}")
            jumlah = input_angka_ulang(
                "Masukkan jumlah lagi : ", minimum=1,
                pesan_min="Jumlah harus lebih dari 0!"
            )

        total = layanan["harga"] * jumlah
        saldo = data_pengguna[username]["saldo"]
        kode_transaksi = "TRX" + str(len(data_transaksi) + 1).zfill(3)

        transaksi = {
            "kode_transaksi": kode_transaksi,
            "username": username,
            "id_layanan": id_layanan,
            "jumlah": jumlah,
            "total": total,
            "waktu": time.strftime("%d-%m-%Y %H:%M:%S")
        }

        print("\n===== INVOICE SEMENTARA =====")
        invoice = PrettyTable()
        invoice.field_names = ["Keterangan", "Detail"]
        invoice.add_row(["Kode Transaksi", kode_transaksi])
        invoice.add_row(["Username", username])
        invoice.add_row(["Jenis Layanan", layanan["jenis"]])
        invoice.add_row(["Harga", f"Rp{layanan['harga']:,}".replace(",", ".")])
        invoice.add_row(["Jumlah", jumlah])
        invoice.add_row(["Total Bayar", f"Rp{total:,}".replace(",", ".")])
        invoice.add_row(["Saldo Anda", f"Rp{saldo:,}".replace(",", ".")])
        print(invoice)

        if saldo < total:
            print("Saldo tidak cukup! Silakan top up.")
            return

        while True:
            try:
                konfirmasi = input("Lanjutkan pembayaran? (y/n): ").strip().lower()
            except KeyboardInterrupt:
                print("\nPeringatan: Ctrl+C terdeteksi. Masukkan y atau n lagi.")
                continue
            if konfirmasi not in ("y", "n"):
                print("Input tidak valid! Masukkan y atau n.")
                continue
            break

        if konfirmasi == "n":
            print("Pesanan dibatalkan.")
            return

        data_pengguna[username]["saldo"] -= total
        layanan["kuota"] -= jumlah
        data_transaksi.append(transaksi)
        save_users()
        save_layanan()

        fieldnames = [
            "kode_transaksi", "username", "id_layanan",
            "jumlah", "total", "waktu"
        ]
        file_baru = (
            not os.path.exists(transaksi_file)
            or os.path.getsize(transaksi_file) == 0
        )
        with open(transaksi_file, "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if file_baru:
                writer.writeheader()
            writer.writerow(transaksi)

        print("\nPembayaran berhasil!")
        cetak_invoice(transaksi)
    except EOFError:
        print("\nPeringatan: Input berakhir (EOF). Pemesanan dibatalkan.")


def riwayat_pesanan(username):
    print("\n===== RIWAYAT PESANAN =====")

    riwayat = []

    for transaksi in data_transaksi:
        if transaksi["username"] == username:
            riwayat.append(transaksi)

    if not riwayat:
        print("Belum ada pesanan.")
        return

    tabel = PrettyTable()

    tabel.field_names = [
        "Kode Transaksi",
        "ID Layanan",
        "Jumlah",
        "Total"
    ]

    for transaksi in riwayat:
        tabel.add_row([
            transaksi["kode_transaksi"],
            transaksi["id_layanan"],
            transaksi["jumlah"],
            transaksi["total"]
        ])

    print(tabel)


def menu_user(username):
    while True:
        print("\n===== MENU USER =====")
        print("1. Lihat Layanan")
        print("2. Pesan Layanan")
        print("3. Top Up")
        print("4. Riwayat Transaksi")
        print("5. Lihat Saldo")
        print("6. Logout")

        try:
            pilihan = input_angka_ulang(
                "Pilih : ", minimum=1, maksimum=6,
                pesan_min="Pilihan tidak tersedia! Masukkan angka 1-6.",
                pesan_max="Pilihan tidak tersedia! Masukkan angka 1-6."
            )
        except EOFError:
            print("\nPeringatan: Input berakhir (EOF).")
            continue

        if pilihan == 1:
            lihat_layanan()
        elif pilihan == 2:
            pesan_layanan(username)
        elif pilihan == 3:
            top_up(username)
        elif pilihan == 4:
            riwayat_pesanan(username)
        elif pilihan == 5:
            print("Saldo : Rp" + f"{data_pengguna[username]['saldo']:,}".replace(",", "."))
        elif pilihan == 6:
            print("Logout berhasil!")
            break


# MENU UTAMA
while True:
    print("\n===== SISTEM LAYANAN IT =====")
    print("1. Registrasi")
    print("2. Login")
    print("3. Keluar")

    try:
        pilihan = input_angka_ulang(
            "Pilih : ", minimum=1, maksimum=3,
            pesan_min="Pilihan tidak tersedia! Masukkan angka 1-3.",
            pesan_max="Pilihan tidak tersedia! Masukkan angka 1-3."
        )
    except EOFError:
        print("\nPeringatan: Input berakhir (EOF). Program dihentikan.")
        break

    if pilihan == 1:
        registrasi()
    elif pilihan == 2:
        login()
    elif pilihan == 3:
        print("Program selesai.")
        break
