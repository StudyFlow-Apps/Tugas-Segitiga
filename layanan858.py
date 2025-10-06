from datetime import datetime, timedelta

masa_aktif = datetime.strptime("30/10/2025", "%d/%m/%Y")

# Mahardika Naufal, Luthfi Iriawan Fadhilah
def menu_beli_masa_aktif():
    global masa_aktif
    while True:
        print(f"\n=== Beli Masa Aktif (saat ini sampai {masa_aktif.strftime('%d/%m/%Y')}) ===")
        print("1. 5hr / Rp2.500")
        print("2. 10hr / Rp4.000")
        print("3. 15hr / Rp6.000")
        print("4. 30hr / Rp14.000")
        print("5. 90hr / Rp33.000")
        print("6. 180hr / Rp62.000")
        print("7. Next")
        print("0. Home")
        print("10. Gift")

        pilihan = input("Masukkan pilihan: ")

        paket = {
            "1": ("5 Hari", 5, 2500),
            "2": ("10 Hari", 10, 4000),
            "3": ("15 Hari", 15, 6000),
            "4": ("30 Hari", 30, 14000),
            "5": ("90 Hari", 90, 33000),
            "6": ("180 Hari", 180, 62000),
        }

        if pilihan in paket:
            durasi_text, durasi_hari, harga = paket[pilihan]
            if konfirmasi_pembelian(durasi_text, harga):
                masa_aktif += timedelta(days=durasi_hari)
                print(f"Masa aktif {durasi_text} berhasil dibeli seharga Rp{harga}.")
                print(f"Masa aktif baru: sampai {masa_aktif.strftime('%d/%m/%Y')}")
            else:
                print("Transaksi dibatalkan.")
        elif pilihan == "0":
            break
        elif pilihan == "7":
            print("Menu selanjutnya belum tersedia (Next Page).")
        elif pilihan == "10":
            print("Menu Gift: Kirim masa aktif ke nomor lain (fitur simulasi).")
        else:
            print("Pilihan tidak valid, coba lagi!")

# Achmad Azhar Fa'iz Sabiq
def konfirmasi_pembelian(durasi, harga):
    while True:
        print(f"\nAnda akan membeli Masa Aktif {durasi} Rp{harga} (Akumulasi Maks 365 Hari)")
        print("1. Ya")
        print("9. Back")
        print("0. Home")

        konfirmasi = input("Masukkan pilihan: ")

        if konfirmasi == "1":
            return True
        elif konfirmasi in ["9", "0"]:
            return False
        else:
            print("Pilihan tidak valid, coba lagi!")

# Jiyad Arsal Asari, Dirgantara Mulyanda
def main_menu():
    while True:
        print("\n=== Layanan Transfer Pulsa ===")
        print("Transfer Pulsamu dan menangkan iPhone 15")
        print("1. Transfer Pulsa")
        print("2. Masa Aktif")
        print("3. Minta Pulsa")
        print("4. Auto TP")
        print("5. Delete Auto TP")
        print("6. List Auto TP")
        print("7. Cek Kupon Undian TP")
        print("0. Keluar")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            nomor = input("Masukkan nomor tujuan: ")
            jumlah = input("Masukkan jumlah pulsa: ")
            print(f"Transfer pulsa Rp{jumlah} ke {nomor} berhasil!")
        elif pilihan == "2":
            menu_beli_masa_aktif()
        elif pilihan == "3":
            nomor = input("Masukkan nomor yang ingin diminta pulsa: ")
            print(f"Permintaan pulsa telah dikirim ke {nomor}")
        elif pilihan == "4":
            nomor = input("Masukkan nomor tujuan Auto TP: ")
            jumlah = input("Masukkan jumlah pulsa: ")
            print(f"Auto Transfer Pulsa Rp{jumlah} ke {nomor} berhasil diaktifkan.")
        elif pilihan == "5":
            print("Auto Transfer Pulsa berhasil dihapus.")
        elif pilihan == "6":
            print("Daftar Auto Transfer Pulsa:\n- 08123456789 : Rp10.000 setiap minggu")
        elif pilihan == "7":
            print("Anda memiliki 5 kupon undian iPhone 15.")
        elif pilihan == "0":
            print("Terima kasih telah menggunakan layanan ini")
            break
        else:
            print("Pilihan tidak valid, coba lagi!")

if __name__ == "__main__":
    main_menu()
