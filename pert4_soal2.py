def tampilkan_menu():
    print("\nPilih aksi:")
    print("1. Tambah tugas")
    print("2. Hapus tugas")
    print("3. Tampilkan daftar tugas")
    print("4. Keluar")

def tambah_tugas(daftar):
    try:
        tugas = input("Masukkan tugas yang ingin ditambahkan: ").strip()
        if not tugas:
            raise ValueError("Tugas tidak boleh kosong.")
        daftar.append(tugas)
        print("Tugas berhasil ditambahkan!")
    except ValueError as e:
        print(f"Error: {e}")

def hapus_tugas(daftar):
    try:
        if not daftar:
            raise Exception("Daftar tugas kosong. Tidak ada yang bisa dihapus.")
        
        for i, tugas in enumerate(daftar, 1):
            print(f"{i}. {tugas}")
        
        nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        if nomor < 1 or nomor > len(daftar):
            raise IndexError(f"Tugas dengan nomor {nomor} tidak ditemukan.")
        
        dihapus = daftar.pop(nomor - 1)
        print(f"Tugas '{dihapus}' berhasil dihapus!")
    
    except ValueError:
        print("Input tidak valid. Masukkan angka yang sesuai.")
    except IndexError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

def tampilkan_tugas(daftar):
    if not daftar:
        print("Daftar tugas kosong.")
    else:
        print("Daftar Tugas:")
        for tugas in daftar:
            print(f"- {tugas}")

def main():
    daftar_tugas = []
    while True:
        tampilkan_menu()
        try:
            pilihan = input("Masukkan pilihan (1/2/3/4): ").strip()
            if pilihan == '1':
                tambah_tugas(daftar_tugas)
            elif pilihan == '2':
                hapus_tugas(daftar_tugas)
            elif pilihan == '3':
                tampilkan_tugas(daftar_tugas)
            elif pilihan == '4':
                print("Keluar dari program.")
                break
            else:
                raise ValueError("Pilihan tidak valid. Masukkan 1, 2, 3, atau 4.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
