import json
import csv
import os

akun_user = "data_pengguna.json"
pesanan_user = "data_pesanan.csv"


def load_users():
    if os.path.exists(akun_user):
        with open(akun_user, "r") as file:
            return json.load(file)
    return {}


def save_users():
    with open(akun_user, "w") as file:
        json.dump(data_pengguna, file, indent=4)


data_pengguna = load_users()



# DATA PESANAN

def load_pesanan():
    if os.path.exists(pesanan_user):
        with open(pesanan_user, "r", newline="") as file:
            return list(csv.DictReader(file))
    return []


def save_pesanan():
    with open(pesanan_user, "w", newline="") as file:

        fieldnames = [
            "nomor_pesanan",
            "username",
            "layanan",
            "deskripsi",
            "tanggal",
            "status"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data_pesanan)


data_pesanan = load_pesanan()


# REGISTRASI

def registrasi():

    print("===== FORM REGISTRASI =====")

    username = input("Username : ")

    if username == "":
        print("Username Tidak Boleh Kosong!")
        return

    if username in data_pengguna:
        print("Username sudah digunakan!")
        return

    nama = input("Nama Lengkap: ")

    if nama == "":
        print("Nama tidak boleh kosong!")
        return

    no_hp = input("Nomor HP: ")

    if no_hp == "":
        print("Nomor HP tidak boleh kosong!")
        return

    password = input("Password (min. 6 karakter): ")

    if len(password) < 6:
        print("Password minimal 6 karakter!")
        return

    data_pengguna[username] = {
        "nama": nama,
        "no_hp": no_hp,
        "password": password
    }

    save_users()

    print(f"Registrasi berhasil! Selamat datang, {nama}!")



# LOGIN

def login():

    print("===== FORM LOGIN =====")

    username = input("Username: ")
    password = input("Password: ")

    if username in data_pengguna:

        if data_pengguna[username]["password"] == password:

            print("Login berhasil!")
            print(f"Hallo, {data_pengguna[username]['nama']}!")

            menu(username)

        else:
            print("Password salah!")

    else:
        print("Username tidak ditemukan.")



# CREATE

def tambah_pesanan(username):

    print("===== TAMBAH PESANAN =====")

    nomor_pesanan = input("Nomor Pesanan : ")

    # Cek ID agar tidak sama
    for pesanan in data_pesanan:

        if pesanan["nomor_pesanan"] == nomor_pesanan:
            print("Nomor Pesanan sudah digunakan!")
            return

    layanan = input("Layanan IT : ")

    if layanan == "":
        print("Layanan tidak boleh kosong!")
        return

    deskripsi = input("Deskripsi masalah : ")

    tanggal = input("Tanggal layanan : ")

    status = "Menunggu"

    data_baru = {
        "nomor_pesanan": nomor_pesanan,
        "username": username,
        "layanan": layanan,
        "deskripsi": deskripsi,
        "tanggal": tanggal,
        "status": status
    }

    data_pesanan.append(data_baru)

    save_pesanan()

    print("Pesanan berhasil ditambahkan!")



# Tampilkan

def lihat_pesanan(username):

    print("===== TAMPILKAN PESANAN =====")

    ditemukan = False

    for pesanan in data_pesanan:

        if pesanan["username"] == username:

            ditemukan = True

            print("Nomor Pesanan :", pesanan["nomor_pesanan"])
            print("Layanan    :", pesanan["layanan"])
            print("Deskripsi  :", pesanan["deskripsi"])
            print("Tanggal    :", pesanan["tanggal"])
            print("Status     :", pesanan["status"])

    if not ditemukan:
        print("Belum ada pesanan.")



# Ubah Pesanan

def ubah_pesanan(username):

    print("===== UBAH PESANAN =====")

    nomor_pesanan = input("Masukkan Nomor Pesanan : ")

    for pesanan in data_pesanan:

        if (
            pesanan["nomor_pesanan"] == nomor_pesanan
            and pesanan["username"] == username
        ):

            print("Data lama:")
            print("Layanan   :", pesanan["layanan"])
            print("Deskripsi :", pesanan["deskripsi"])
            print("Tanggal   :", pesanan["tanggal"])

            print("Masukkan data baru:")

            layanan_baru = input("Layanan baru : ")
            deskripsi_baru = input("Deskripsi baru : ")
            tanggal_baru = input("Tanggal baru : ")

            if layanan_baru != "":
                pesanan["layanan"] = layanan_baru

            if deskripsi_baru != "":
                pesanan["deskripsi"] = deskripsi_baru

            if tanggal_baru != "":
                pesanan["tanggal"] = tanggal_baru

            save_pesanan()

            print("Pesanan berhasil diperbarui!")

            return

    print("Pesanan tidak ditemukan.")



# HAPUS

def hapus_pesanan(username):

    print("HAPUS PESANAN")

    nomor_pesanan = input("Masukkan Nomor Pesanan : ")

    for pesanan in data_pesanan:

        if (
            pesanan["nomor_pesanan"] == nomor_pesanan
            and pesanan["username"] == username
        ):

            data_pesanan.remove(pesanan)

            save_pesanan()

            print("Pesanan berhasil dihapus!")

            return

    print("Pesanan tidak ditemukan.")



# MENU

def menu(username):

    while True:
        print("MENU PESANAN IT")

        print("1. Tambah Pesanan")
        print("2. Lihat Pesanan")
        print("3. Ubah Pesanan")
        print("4. Hapus Pesanan")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_pesanan(username)

        elif pilihan == "2":
            lihat_pesanan(username)

        elif pilihan == "3":
            ubah_pesanan(username)

        elif pilihan == "4":
            hapus_pesanan(username)

        elif pilihan == "5":
            print("Keluar dari menu CRUD.")
            break

        else:
            print("Pilihan tidak valid!")



# MENU UTAMA

while True:
    print("SISTEM PEMESANAN LAYANAN IT")

    print("1. Registrasi Akun")
    print("2. Login Akun")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        registrasi()

    elif pilihan == "2":
        login()

    elif pilihan == "3":
        print("Terima Kasih! Sampai jumpa.")
        break

    else:
        print("Pilihan tidak valid!")