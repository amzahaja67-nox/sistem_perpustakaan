import os
from datetime import datetime, timedelta


FILE_BUKU = "data_buku.txt"
FILE_ANGGOTA = "data_anggota.txt"
FILE_TRANSAKSI = "data_transaksi.txt"
FILE_USER = "data_user.txt"
FILE_LAPORAN = "laporan_perpustakaan.txt"

DENDA_PER_HARI = 2000
LAMA_PINJAM = 7



buku = []
anggota = []
transaksi = []
users = []



def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nTekan ENTER untuk melanjutkan...")


def tanggal_sekarang():
    return datetime.now().strftime("%Y-%m-%d")


def waktu_sekarang():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def generate_id(prefix, data):
    """
    Membuat ID otomatis.
    Contoh:
    BK001
    AG001
    TR001
    """
    nomor_terbesar = 0

    for item in data:
        try:
            nomor = int(item["id"][2:])
            if nomor > nomor_terbesar:
                nomor_terbesar = nomor
        except:
            continue

    return f"{prefix}{nomor_terbesar + 1:03d}"



def load_users():
    global users

    if not os.path.exists(FILE_USER):
        users.append({
            "username": "amzah_aja25",
            "password": "kholilul0806",
            "nama": "Amzahazka"
        })

        save_users()
        return

    with open(FILE_USER, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()

            if baris:
                try:
                    username, password, nama = baris.split("|")

                    users.append({
                        "username": username,
                        "password": password,
                        "nama": nama
                    })

                except:
                    continue


def save_users():
    with open(FILE_USER, "w", encoding="utf-8") as file:
        for user in users:
            file.write(
                f"{user['username']}|"
                f"{user['password']}|"
                f"{user['nama']}\n"
            )


def load_buku():
    global buku

    if not os.path.exists(FILE_BUKU):
        return

    with open(FILE_BUKU, "r", encoding="utf-8") as file:

        for baris in file:
            baris = baris.strip()

            if baris:
                try:
                    id_buku, judul, penulis, tahun, kategori, status = baris.split("|")

                    buku.append({
                        "id": id_buku,
                        "judul": judul,
                        "penulis": penulis,
                        "tahun": tahun,
                        "kategori": kategori,
                        "status": status
                    })

                except:
                    continue


def save_buku():
    with open(FILE_BUKU, "w", encoding="utf-8") as file:

        for data in buku:
            file.write(
                f"{data['id']}|"
                f"{data['judul']}|"
                f"{data['penulis']}|"
                f"{data['tahun']}|"
                f"{data['kategori']}|"
                f"{data['status']}\n"
            )


def load_anggota():
    global anggota

    if not os.path.exists(FILE_ANGGOTA):
        return

    with open(FILE_ANGGOTA, "r", encoding="utf-8") as file:

        for baris in file:
            baris = baris.strip()

            if baris:
                try:
                    id_anggota, nama, nim, kelas, no_hp = baris.split("|")

                    anggota.append({
                        "id": id_anggota,
                        "nama": nama,
                        "nim": nim,
                        "kelas": kelas,
                        "no_hp": no_hp
                    })

                except:
                    continue


def save_anggota():
    with open(FILE_ANGGOTA, "w", encoding="utf-8") as file:

        for data in anggota:
            file.write(
                f"{data['id']}|"
                f"{data['nama']}|"
                f"{data['nim']}|"
                f"{data['kelas']}|"
                f"{data['no_hp']}\n"
            )


def load_transaksi():
    global transaksi

    if not os.path.exists(FILE_TRANSAKSI):
        return

    with open(FILE_TRANSAKSI, "r", encoding="utf-8") as file:

        for baris in file:
            baris = baris.strip()

            if baris:
                try:

                    (
                        id_transaksi,
                        id_buku,
                        id_anggota,
                        tanggal_pinjam,
                        batas_kembali,
                        tanggal_kembali,
                        status,
                        denda
                    ) = baris.split("|")

                    transaksi.append({
                        "id": id_transaksi,
                        "id_buku": id_buku,
                        "id_anggota": id_anggota,
                        "tanggal_pinjam": tanggal_pinjam,
                        "batas_kembali": batas_kembali,
                        "tanggal_kembali": tanggal_kembali,
                        "status": status,
                        "denda": denda
                    })

                except:
                    continue


def save_transaksi():

    with open(FILE_TRANSAKSI, "w", encoding="utf-8") as file:

        for data in transaksi:

            file.write(
                f"{data['id']}|"
                f"{data['id_buku']}|"
                f"{data['id_anggota']}|"
                f"{data['tanggal_pinjam']}|"
                f"{data['batas_kembali']}|"
                f"{data['tanggal_kembali']}|"
                f"{data['status']}|"
                f"{data['denda']}\n"
            )



def login():

    kesempatan = 3

    while kesempatan > 0:

        clear_screen()

        print("=" * 50)
        print("          LOGIN SISTEM PERPUSTAKAAN")
        print("=" * 50)

        username = input("Username : ")
        password = input("Password : ")

        for user in users:

            if (
                user["username"] == username
                and user["password"] == password
            ):

                print("\nLogin berhasil!")
                print(f"Selamat datang, {user['nama']}.")

                pause()

                return user

        kesempatan -= 1

        print("\nUsername atau password salah!")
        print(f"Sisa percobaan: {kesempatan}")

        pause()

    print("\nAkses ditolak.")
    return None



def dashboard():

    total_buku = len(buku)

    tersedia = sum(
        1 for data in buku
        if data["status"] == "Tersedia"
    )

    dipinjam = sum(
        1 for data in buku
        if data["status"] == "Dipinjam"
    )

    total_anggota = len(anggota)

    total_denda = sum(
        int(data["denda"])
        for data in transaksi
    )

    print("=" * 65)
    print("                    DASHBOARD")
    print("=" * 65)

    print(f"Total Buku       : {total_buku}")
    print(f"Buku Tersedia    : {tersedia}")
    print(f"Buku Dipinjam    : {dipinjam}")
    print(f"Total Anggota    : {total_anggota}")
    print(f"Total Transaksi  : {len(transaksi)}")
    print(f"Total Denda      : Rp{total_denda:,}".replace(",", "."))

    print("=" * 65)



def tambah_buku():

    clear_screen()

    print("=" * 50)
    print("                  TAMBAH BUKU")
    print("=" * 50)

    judul = input("Judul Buku     : ").strip()
    penulis = input("Penulis        : ").strip()
    tahun = input("Tahun Terbit   : ").strip()
    kategori = input("Kategori       : ").strip()

    if not judul:
        print("Judul buku tidak boleh kosong.")
        pause()
        return

    id_buku = generate_id("BK", buku)

    buku.append({
        "id": id_buku,
        "judul": judul,
        "penulis": penulis,
        "tahun": tahun,
        "kategori": kategori,
        "status": "Tersedia"
    })

    save_buku()

    print("\nBuku berhasil ditambahkan.")
    print(f"ID Buku : {id_buku}")

    pause()


def lihat_buku():

    clear_screen()

    print("=" * 90)
    print("                         DAFTAR BUKU")
    print("=" * 90)

    if not buku:
        print("Belum ada data buku.")
        pause()
        return

    print(
        f"{'No':<4}"
        f"{'ID':<8}"
        f"{'Judul':<25}"
        f"{'Penulis':<20}"
        f"{'Tahun':<8}"
        f"{'Status':<12}"
    )

    print("-" * 90)

    for i, data in enumerate(buku, 1):

        print(
            f"{i:<4}"
            f"{data['id']:<8}"
            f"{data['judul'][:23]:<25}"
            f"{data['penulis'][:18]:<20}"
            f"{data['tahun']:<8}"
            f"{data['status']:<12}"
        )

    pause()


def cari_buku():

    clear_screen()

    print("=" * 50)
    print("                    CARI BUKU")
    print("=" * 50)

    keyword = input("Masukkan judul/kategori/penulis: ").lower()

    hasil = []

    for data in buku:

        if (
            keyword in data["judul"].lower()
            or keyword in data["penulis"].lower()
            or keyword in data["kategori"].lower()
        ):

            hasil.append(data)

    if not hasil:
        print("\nBuku tidak ditemukan.")
        pause()
        return

    print("\nHasil pencarian:")
    print("-" * 80)

    for data in hasil:

        print(
            f"{data['id']} | "
            f"{data['judul']} | "
            f"{data['penulis']} | "
            f"{data['kategori']} | "
            f"{data['status']}"
        )

    pause()


def edit_buku():

    clear_screen()

    lihat_buku()

    id_buku = input("\nMasukkan ID buku yang ingin diedit: ").upper()

    for data in buku:

        if data["id"] == id_buku:

            print("\nKosongkan input jika tidak ingin mengubah data.")

            judul = input(f"Judul [{data['judul']}]: ")
            penulis = input(f"Penulis [{data['penulis']}]: ")
            tahun = input(f"Tahun [{data['tahun']}]: ")
            kategori = input(f"Kategori [{data['kategori']}]: ")

            if judul:
                data["judul"] = judul

            if penulis:
                data["penulis"] = penulis

            if tahun:
                data["tahun"] = tahun

            if kategori:
                data["kategori"] = kategori

            save_buku()

            print("\nData buku berhasil diperbarui.")

            pause()
            return

    print("ID buku tidak ditemukan.")
    pause()


def hapus_buku():

    clear_screen()

    lihat_buku()

    id_buku = input("\nMasukkan ID buku yang ingin dihapus: ").upper()

    for data in buku:

        if data["id"] == id_buku:

            if data["status"] == "Dipinjam":
                print("Buku sedang dipinjam dan tidak dapat dihapus.")
                pause()
                return

            konfirmasi = input(
                f"Yakin menghapus '{data['judul']}'? (y/n): "
            ).lower()

            if konfirmasi == "y":

                buku.remove(data)
                save_buku()

                print("Buku berhasil dihapus.")

            else:
                print("Penghapusan dibatalkan.")

            pause()
            return

    print("ID buku tidak ditemukan.")
    pause()


def menu_buku():

    while True:

        clear_screen()

        print("=" * 50)
        print("               MANAJEMEN BUKU")
        print("=" * 50)

        print("1. Tambah Buku")
        print("2. Lihat Buku")
        print("3. Cari Buku")
        print("4. Edit Buku")
        print("5. Hapus Buku")
        print("6. Kembali")

        pilihan = input("\nPilih menu: ")

        if pilihan == "1":
            tambah_buku()

        elif pilihan == "2":
            lihat_buku()

        elif pilihan == "3":
            cari_buku()

        elif pilihan == "4":
            edit_buku()

        elif pilihan == "5":
            hapus_buku()

        elif pilihan == "6":
            break

        else:
            print("Pilihan tidak valid.")
            pause()



def tambah_anggota():

    clear_screen()

    print("=" * 50)
    print("                TAMBAH ANGGOTA")
    print("=" * 50)

    nama = input("Nama Lengkap : ").strip()
    nim = input("NIM          : ").strip()
    kelas = input("Kelas        : ").strip()
    no_hp = input("No. HP       : ").strip()

    if not nama or not nim:
        print("Nama dan NIM wajib diisi.")
        pause()
        return

    id_anggota = generate_id("AG", anggota)

    anggota.append({
        "id": id_anggota,
        "nama": nama,
        "nim": nim,
        "kelas": kelas,
        "no_hp": no_hp
    })

    save_anggota()

    print("\nAnggota berhasil ditambahkan.")
    print(f"ID Anggota : {id_anggota}")

    pause()


def lihat_anggota():

    clear_screen()

    print("=" * 90)
    print("                       DAFTAR ANGGOTA")
    print("=" * 90)

    if not anggota:
        print("Belum ada data anggota.")
        pause()
        return

    print(
        f"{'No':<4}"
        f"{'ID':<8}"
        f"{'Nama':<25}"
        f"{'NIM':<15}"
        f"{'Kelas':<15}"
        f"{'No HP':<15}"
    )

    print("-" * 90)

    for i, data in enumerate(anggota, 1):

        print(
            f"{i:<4}"
            f"{data['id']:<8}"
            f"{data['nama'][:23]:<25}"
            f"{data['nim']:<15}"
            f"{data['kelas']:<15}"
            f"{data['no_hp']:<15}"
        )

    pause()


def cari_anggota():

    clear_screen()

    keyword = input("Masukkan nama/NIM anggota: ").lower()

    hasil = []

    for data in anggota:

        if (
            keyword in data["nama"].lower()
            or keyword in data["nim"].lower()
        ):
            hasil.append(data)

    if not hasil:
        print("\nAnggota tidak ditemukan.")
        pause()
        return

    print("\nHasil pencarian:")

    for data in hasil:

        print(
            f"{data['id']} | "
            f"{data['nama']} | "
            f"{data['nim']} | "
            f"{data['kelas']}"
        )

    pause()


def hapus_anggota():

    clear_screen()

    lihat_anggota()

    id_anggota = input(
        "\nMasukkan ID anggota yang ingin dihapus: "
    ).upper()

    for data in anggota:

        if data["id"] == id_anggota:

            # Cek apakah anggota masih memiliki buku
            for trx in transaksi:

                if (
                    trx["id_anggota"] == id_anggota
                    and trx["status"] == "Dipinjam"
                ):

                    print(
                        "Anggota masih memiliki buku yang dipinjam."
                    )

                    pause()
                    return

            konfirmasi = input(
                f"Yakin menghapus {data['nama']}? (y/n): "
            ).lower()

            if konfirmasi == "y":

                anggota.remove(data)
                save_anggota()

                print("Anggota berhasil dihapus.")

            pause()
            return

    print("ID anggota tidak ditemukan.")
    pause()


def menu_anggota():

    while True:

        clear_screen()

        print("=" * 50)
        print("             MANAJEMEN ANGGOTA")
        print("=" * 50)

        print("1. Tambah Anggota")
        print("2. Lihat Anggota")
        print("3. Cari Anggota")
        print("4. Hapus Anggota")
        print("5. Kembali")

        pilihan = input("\nPilih menu: ")

        if pilihan == "1":
            tambah_anggota()

        elif pilihan == "2":
            lihat_anggota()

        elif pilihan == "3":
            cari_anggota()

        elif pilihan == "4":
            hapus_anggota()

        elif pilihan == "5":
            break

        else:
            print("Pilihan tidak valid.")
            pause()



def pinjam_buku():

    clear_screen()

    print("=" * 60)
    print("                    PEMINJAMAN BUKU")
    print("=" * 60)

    if not buku:
        print("Belum ada buku.")
        pause()
        return

    if not anggota:
        print("Belum ada anggota.")
        pause()
        return

    id_anggota = input("ID Anggota : ").upper()
    id_buku = input("ID Buku    : ").upper()

    anggota_ditemukan = None
    buku_ditemukan = None

    for data in anggota:

        if data["id"] == id_anggota:
            anggota_ditemukan = data

    for data in buku:

        if data["id"] == id_buku:
            buku_ditemukan = data

    if anggota_ditemukan is None:
        print("Anggota tidak ditemukan.")
        pause()
        return

    if buku_ditemukan is None:
        print("Buku tidak ditemukan.")
        pause()
        return

    if buku_ditemukan["status"] == "Dipinjam":
        print("Buku sedang dipinjam.")
        pause()
        return

    jumlah_pinjam = 0

    for trx in transaksi:

        if (
            trx["id_anggota"] == id_anggota
            and trx["status"] == "Dipinjam"
        ):

            jumlah_pinjam += 1

    if jumlah_pinjam >= 3:

        print(
            "Anggota sudah mencapai maksimal "
            "3 buku yang sedang dipinjam."
        )

        pause()
        return

    tanggal_pinjam = datetime.now()
    batas_kembali = tanggal_pinjam + timedelta(days=LAMA_PINJAM)

    id_transaksi = generate_id("TR", transaksi)

    transaksi.append({

        "id": id_transaksi,
        "id_buku": id_buku,
        "id_anggota": id_anggota,
        "tanggal_pinjam": tanggal_pinjam.strftime("%Y-%m-%d"),
        "batas_kembali": batas_kembali.strftime("%Y-%m-%d"),
        "tanggal_kembali": "-",
        "status": "Dipinjam",
        "denda": "0"

    })

    buku_ditemukan["status"] = "Dipinjam"

    save_buku()
    save_transaksi()

    print("\nPeminjaman berhasil.")

    print(f"ID Transaksi   : {id_transaksi}")
    print(f"Buku           : {buku_ditemukan['judul']}")
    print(f"Peminjam       : {anggota_ditemukan['nama']}")
    print(f"Tanggal Pinjam : {tanggal_pinjam.strftime('%Y-%m-%d')}")
    print(f"Batas Kembali  : {batas_kembali.strftime('%Y-%m-%d')}")

    cetak_struk(id_transaksi)

    pause()



def kembalikan_buku():

    clear_screen()

    print("=" * 60)
    print("                   PENGEMBALIAN BUKU")
    print("=" * 60)

    id_transaksi = input("ID Transaksi: ").upper()

    trx_ditemukan = None

    for trx in transaksi:

        if trx["id"] == id_transaksi:

            trx_ditemukan = trx

    if trx_ditemukan is None:
        print("Transaksi tidak ditemukan.")
        pause()
        return

    if trx_ditemukan["status"] != "Dipinjam":
        print("Transaksi sudah selesai.")
        pause()
        return

    tanggal_kembali = datetime.now()

    batas_kembali = datetime.strptime(
        trx_ditemukan["batas_kembali"],
        "%Y-%m-%d"
    )

    keterlambatan = (tanggal_kembali - batas_kembali).days

    if keterlambatan < 0:
        keterlambatan = 0

    denda = keterlambatan * DENDA_PER_HARI

    trx_ditemukan["tanggal_kembali"] = tanggal_kembali.strftime(
        "%Y-%m-%d"
    )

    trx_ditemukan["status"] = "Dikembalikan"

    trx_ditemukan["denda"] = str(denda)

    for data in buku:

        if data["id"] == trx_ditemukan["id_buku"]:

            data["status"] = "Tersedia"

            judul_buku = data["judul"]

            break

    save_buku()
    save_transaksi()

    print("\nBuku berhasil dikembalikan.")

    print(f"Buku          : {judul_buku}")
    print(f"Tanggal Kembali : {tanggal_kembali.strftime('%Y-%m-%d')}")
    print(f"Keterlambatan : {keterlambatan} hari")
    print(f"Denda         : Rp{denda:,}".replace(",", "."))

    cetak_struk(id_transaksi)

    pause()



def perpanjangan():

    clear_screen()

    print("=" * 60)
    print("                 PERPANJANGAN PEMINJAMAN")
    print("=" * 60)

    id_transaksi = input("ID Transaksi: ").upper()

    for trx in transaksi:

        if trx["id"] == id_transaksi:

            if trx["status"] != "Dipinjam":
                print("Transaksi sudah selesai.")
                pause()
                return

            batas_lama = datetime.strptime(
                trx["batas_kembali"],
                "%Y-%m-%d"
            )

            batas_baru = batas_lama + timedelta(days=7)

            trx["batas_kembali"] = batas_baru.strftime(
                "%Y-%m-%d"
            )

            save_transaksi()

            print("\nPeminjaman berhasil diperpanjang.")
            print(
                f"Batas pengembalian baru: "
                f"{trx['batas_kembali']}"
            )

            pause()
            return

    print("Transaksi tidak ditemukan.")
    pause()



def riwayat_transaksi():

    clear_screen()

    print("=" * 100)
    print("                         RIWAYAT TRANSAKSI")
    print("=" * 100)

    if not transaksi:
        print("Belum ada transaksi.")
        pause()
        return

    for trx in transaksi:

        nama_buku = "-"
        nama_anggota = "-"

        for data in buku:

            if data["id"] == trx["id_buku"]:
                nama_buku = data["judul"]

        for data in anggota:

            if data["id"] == trx["id_anggota"]:
                nama_anggota = data["nama"]

        print("-" * 100)

        print(f"ID Transaksi   : {trx['id']}")
        print(f"Buku           : {nama_buku}")
        print(f"Anggota        : {nama_anggota}")
        print(f"Tanggal Pinjam : {trx['tanggal_pinjam']}")
        print(f"Batas Kembali  : {trx['batas_kembali']}")
        print(f"Tanggal Kembali: {trx['tanggal_kembali']}")
        print(f"Status         : {trx['status']}")
        print(
            f"Denda          : Rp{int(trx['denda']):,}"
            .replace(",", ".")
        )

    pause()



def cetak_struk(id_transaksi):

    trx = None

    for data in transaksi:

        if data["id"] == id_transaksi:
            trx = data
            break

    if trx is None:
        return

    nama_buku = "-"
    nama_anggota = "-"

    for data in buku:

        if data["id"] == trx["id_buku"]:
            nama_buku = data["judul"]

    for data in anggota:

        if data["id"] == trx["id_anggota"]:
            nama_anggota = data["nama"]

    nama_file = f"struk_{id_transaksi}.txt"

    with open(nama_file, "w", encoding="utf-8") as file:

        file.write("=" * 40 + "\n")
        file.write("       PERPUSTAKAAN DIGITAL\n")
        file.write("=" * 40 + "\n")

        file.write(f"ID Transaksi : {trx['id']}\n")
        file.write(f"Anggota      : {nama_anggota}\n")
        file.write(f"Buku         : {nama_buku}\n")
        file.write(f"Tgl Pinjam   : {trx['tanggal_pinjam']}\n")
        file.write(f"Batas Kembali: {trx['batas_kembali']}\n")
        file.write(f"Tgl Kembali  : {trx['tanggal_kembali']}\n")
        file.write(f"Status       : {trx['status']}\n")

        file.write(
            f"Denda        : Rp{int(trx['denda']):,}\n"
            .replace(",", ".")
        )

        file.write("=" * 40 + "\n")
        file.write("Terima kasih telah menggunakan\n")
        file.write("Sistem Perpustakaan.\n")
        file.write("=" * 40 + "\n")

    print(f"\nStruk disimpan sebagai: {nama_file}")



def laporan():

    clear_screen()

    print("=" * 60)
    print("                 LAPORAN PERPUSTAKAAN")
    print("=" * 60)

    total_buku = len(buku)

    tersedia = sum(
        1 for data in buku
        if data["status"] == "Tersedia"
    )

    dipinjam = sum(
        1 for data in buku
        if data["status"] == "Dipinjam"
    )

    total_denda = sum(
        int(data["denda"])
        for data in transaksi
    )

    with open(FILE_LAPORAN, "w", encoding="utf-8") as file:

        file.write("=" * 70 + "\n")
        file.write("              LAPORAN SISTEM PERPUSTAKAAN\n")
        file.write("=" * 70 + "\n")

        file.write(
            f"Tanggal laporan : {waktu_sekarang()}\n\n"
        )

        file.write(f"Total Buku      : {total_buku}\n")
        file.write(f"Buku Tersedia   : {tersedia}\n")
        file.write(f"Buku Dipinjam   : {dipinjam}\n")
        file.write(f"Total Anggota   : {len(anggota)}\n")
        file.write(f"Total Transaksi : {len(transaksi)}\n")
        file.write(
            f"Total Denda     : Rp{total_denda:,}\n"
            .replace(",", ".")
        )

        file.write("\n")
        file.write("=" * 70 + "\n")
        file.write("DAFTAR BUKU\n")
        file.write("=" * 70 + "\n")

        for i, data in enumerate(buku, 1):

            file.write(
                f"{i}. {data['id']} | "
                f"{data['judul']} | "
                f"{data['penulis']} | "
                f"{data['kategori']} | "
                f"{data['status']}\n"
            )

        file.write("\n")
        file.write("=" * 70 + "\n")
        file.write("DATA ANGGOTA\n")
        file.write("=" * 70 + "\n")

        for i, data in enumerate(anggota, 1):

            file.write(
                f"{i}. {data['id']} | "
                f"{data['nama']} | "
                f"{data['nim']} | "
                f"{data['kelas']}\n"
            )

        file.write("\n")
        file.write("=" * 70 + "\n")
        file.write("RIWAYAT TRANSAKSI\n")
        file.write("=" * 70 + "\n")

        for data in transaksi:

            file.write(
                f"{data['id']} | "
                f"Buku: {data['id_buku']} | "
                f"Anggota: {data['id_anggota']} | "
                f"{data['status']} | "
                f"Denda: Rp{data['denda']}\n"
            )

        file.write("=" * 70 + "\n")

    print("Laporan berhasil dibuat.")
    print(f"File: {FILE_LAPORAN}")

    pause()



def menu_transaksi():

    while True:

        clear_screen()

        print("=" * 50)
        print("              MENU TRANSAKSI")
        print("=" * 50)

        print("1. Pinjam Buku")
        print("2. Kembalikan Buku")
        print("3. Perpanjang Peminjaman")
        print("4. Riwayat Transaksi")
        print("5. Kembali")

        pilihan = input("\nPilih menu: ")

        if pilihan == "1":
            pinjam_buku()

        elif pilihan == "2":
            kembalikan_buku()

        elif pilihan == "3":
            perpanjangan()

        elif pilihan == "4":
            riwayat_transaksi()

        elif pilihan == "5":
            break

        else:
            print("Pilihan tidak valid.")
            pause()



def menu_utama(user):

    while True:

        clear_screen()

        print("=" * 65)
        print("             SISTEM INFORMASI PERPUSTAKAAN")
        print("=" * 65)

        print(f"Petugas : {user['nama']}")
        print(f"Tanggal : {tanggal_sekarang()}")

        print("-" * 65)

        dashboard()

        print("\nMENU UTAMA")
        print("1. Manajemen Buku")
        print("2. Manajemen Anggota")
        print("3. Transaksi")
        print("4. Laporan")
        print("5. Logout")
        print("6. Keluar Sistem")

        pilihan = input("\nPilih menu: ")

        if pilihan == "1":
            menu_buku()

        elif pilihan == "2":
            menu_anggota()

        elif pilihan == "3":
            menu_transaksi()

        elif pilihan == "4":
            laporan()

        elif pilihan == "5":
            print("\nLogout berhasil.")
            pause()
            return "logout"

        elif pilihan == "6":

            print("\nTerima kasih telah menggunakan sistem.")

            return "exit"

        else:

            print("\nPilihan tidak valid.")
            pause()




load_users()
load_buku()
load_anggota()
load_transaksi()


while True:

    user_login = login()

    if user_login is None:
        break

    hasil = menu_utama(user_login)

    if hasil == "exit":
        break