from tabulate import tabulate

mobil = {
    "B5012WCD": ["Toyota Alphard", 1500000, 'Tersedia'],
    "B5012WCA": ["Toyota Hiace", 1200000, 'Tersedia'],
    "B5012WCX": ["Toyota Camry", 1500000, 'Disewa'],
}

# menampilkan menu utama
def tampilkan_menu():
    
    print("======== SELAMAT DATANG ========")
    print("          RENTAL MOBIL          ") 
    print("          === MENU ===          ")
    print("1. Tampilkan Data Mobil")
    print("2. Tambah Data Mobil")
    print("3. Ubah Data Mobil")
    print("4. Hapus Data Mobil")
    print("5. Exit Program")
    
    return input("Pilih menu yang ingin dijalankan: ")

# menampilkan semua data mobil 
def tampilkan_daftar():
    tabel_kendaraan = []
    
    for index, plat in enumerate(mobil, start=1): 
        nama = mobil[plat][0]
        harga = mobil[plat][1]
        status = mobil[plat][2]
        tabel_kendaraan.append([index, plat, nama, f"Rp{harga:,.0f}", status])

    print("\nDaftar Mobil")
    print(tabulate(tabel_kendaraan, headers=["No.", "Plat Nomor", "Nama Kendaraan", "Harga Sewa / Hari", "Status"], tablefmt="grid"))

# sub menu untuk menampilkan data mobil
def menu_tampilkan_data():
    while True:
        global mobil
        if not mobil:
            print("\nDatabase mobil kosong. Tidak ada data untuk ditampilkan.")
            return

        print("\n--- SUB MENU TAMPILKAN DATA ---")
        print("1. Tampilkan Semua Mobil")
        print("2. Cari Mobil Berdasarkan Plat TNKB")
        print("3. Kembali ke Menu Utama")
        pilihan = input("Pilih menu (1/2/3): ").strip()

        if pilihan == "1":
            tampilkan_daftar()
        
        elif pilihan == "2":
            while True:
                plat_cari = input("Masukkan Plat TNKB yang ingin dicari (atau 'Batal'): ").upper().strip().replace(' ', '')

                if plat_cari == 'BATAL':
                    break

                if plat_cari in mobil:
                    data = mobil[plat_cari]
                    print(f"\n--- HASIL PENCARIAN ({plat_cari}) ---")
                    print(f"Nama Mobil  : {data[0]}")
                    print(f"Harga Sewa  : Rp{data[1]:,.0f}")
                    print(f"Status Unit : {data[2]}")
                    print("--------------------------------------")
                    break
                else:
                    print(f"\nData Kendaraan dengan Plat TNKB '{plat_cari}' tidak ditemukan.")
                    continue
        
        elif pilihan == "3":
            print("Kembali ke menu utama.")
            return
        else:
            print("Pilihan tidak valid.")

# function untuk menambah data mobil
def tambah_mobil():
    global mobil
    tampilkan_daftar()
    
    while True:
        plat_input = input("Masukkan Plat TNKB (Cth: B1234ABC): ").upper().strip().replace(' ','')

        if not plat_input:
            print("Plat TNKB tidak boleh kosong. Mohon diisi.")
            continue
        
        if plat_input.isdigit():
            print("Plat TNKB tidak valid. Harus mengandung huruf seperti kode wilayah di depan dan huruf akhir maks. 3.")
            continue

        if plat_input.isalpha():
            print("Plat TNKB tidak valid. Harus mengandung angka.")
            continue

        if not plat_input.isalnum():
            print("Plat TNKB tidak valid. Hanya boleh mengandung huruf dan angka.")
            continue

        if plat_input in mobil:
            print(f"Mobil dengan TNKB {plat_input} sudah ada di database!")
            print("Silakan masukkan Plat TNKB lain.")
            continue 

        break
    
    while True:
        nama_input = input("Masukkan Nama Kendaraan: ").title()
        if nama_input.isdigit():
            print("Nama kendaraan tidak boleh hanya angka.")
            continue
        if not nama_input.strip():
            print("Nama kendaraan tidak boleh kosong.")
            continue
        break
    
    while True:
        harga_input = input("Masukkan Harga Sewa / Hari : ")

        if not harga_input.strip():
            print("Harga sewa tidak boleh kosong. Mohon diisi.")
            continue
        
        if harga_input.isdigit() and int(harga_input) > 0:
            harga_sewa = int(harga_input)
            break
        else:
            print("Harga sewa harus diisi dengan angka bulat positif")

    
    while True:
        status_input = input("Masukkan Status Unit (Tersedia / Disewa): ").upper()

        if not status_input.strip():
            print("Status input tidak boleh kosong. Mohon diisi 'Tersedia' atau 'Disewa'.")
            continue
        
        if status_input == "TERSEDIA" or status_input == "DISEWA":
            status_unit = status_input.title()
            break
        else:
            print("Status harus diisi 'Tersedia' atau 'Disewa'.")
    
    konfirm_simpan = input("\nYakin ingin menyimpan data mobil baru ini? (Y/N) : ").upper()

    if konfirm_simpan == "Y":
        mobil[plat_input] = [nama_input, harga_sewa, status_unit]
        tampilkan_daftar()
        print(f"\nMobil {nama_input} dengan No. TNKB {plat_input} berhasil ditambahkan!")
    else:
        print("\nPenambahan data dibatalkan.")

# function untuk mengubah data mobil
def ubah_mobil():
    global mobil
    
    if not mobil:
        print("Database mobil kosong, tidak ada data untuk diubah.")
        return
        
    tampilkan_daftar()

    while True:
        plat_ubah = input("Masukkan Nomor Plat TNKB yang ingin diubah (atau 'Batal' untuk batal): ").upper().strip().replace(' ', '')

        if plat_ubah == 'BATAL':
            print("\nUpdate data dibatalkan.")
            return

        if plat_ubah in mobil:
            break
        else:
            print(f"\nPlat TNKB '{plat_ubah}' tidak ditemukan! Silakan coba lagi atau ketik 'Batal' untuk batal.")
            continue

    data_lama = mobil[plat_ubah]
    nama_lama_awal = data_lama[0]
    
    print(f"\nMobil {nama_lama_awal} dengan Plat {plat_ubah} ditemukan.")
    konfirmasi_lanjut = input("Lanjutkan perubahan data? (Y/N): ").upper()
    if konfirmasi_lanjut != "Y":
        print("\nUpdate data dibatalkan.")
        return
    
    ubah = False
    
    while True:
        nama_saat_ini = mobil[plat_ubah][0]
        harga_saat_ini = mobil[plat_ubah][1]
        status_saat_ini = mobil[plat_ubah][2]

        pilih_kolom = input(
            f"\n--- DATA SAAT INI ({plat_ubah}) ---\n"
            f"1. Nama Mobil : {nama_saat_ini}\n"
            f"2. Harga Sewa : Rp{harga_saat_ini:,.0f}\n"
            f"3. Status Unit  : {status_saat_ini}\n"
            "-----------------------------------\n"
            "Pilih kolom yang ingin diubah:\n"
            "1. Nama Mobil\n"
            "2. Harga Sewa\n"
            "3. Status Unit\n"
            "4. Selesai (Simpan Perubahan)\n" 
            "Pilih menu (1/2/3/4): "
        ).strip()

        if pilih_kolom == "4":
            break

        elif pilih_kolom == "1":
            while True:
                nama_baru = input(f"Masukkan Nama Mobil baru (Nama lama: {nama_saat_ini}): ").title().strip()
                
                if not nama_baru:
                    konfirm_batal = input("Nama mobil tidak boleh kosong. Batalkan perubahan? (Y/N): ").upper()
                    if konfirm_batal == "Y":
                        print("Perubahan Nama dibatalkan.")
                        break
                    continue

                if nama_baru.isdigit():
                    print("Nama mobil tidak boleh hanya angka.")
                    continue
                
                konfirm_simpan = input(f"Yakin ingin mengubah Nama menjadi '{nama_baru}'? (Y/N): ").upper()
                if konfirm_simpan == "Y":
                    mobil[plat_ubah][0] = nama_baru
                    ubah = True
                    print(f"Nama berhasil diubah menjadi: {nama_baru}")
                break

        elif pilih_kolom == "2":
            while True:
                harga_input = input(f"Masukkan Harga Sewa baru (lama: Rp{harga_saat_ini:,.0f}) [Kosongkan untuk batal]: ").strip()
                if not harga_input:
                    print("Perubahan harga sewa dibatalkan.")
                    break
                
                if harga_input.isdigit() and int(harga_input) > 0:
                    
                    konfirm_simpan = input(f"Yakin ingin mengubah Harga Sewa menjadi Rp{int(harga_input):,.0f}? (Y/N): ").upper()
                    if konfirm_simpan == "Y":
                        mobil[plat_ubah][1] = int(harga_input)
                        ubah = True
                        print(f"Harga Sewa berhasil diubah menjadi: Rp{int(harga_input):,.0f}")
                    break
                else:
                    print("Harga sewa harus angka bulat positif dan angka saja.")
            
        elif pilih_kolom == "3":
            while True:
                status_input = input(f"Masukkan Status Unit baru (Status Unit lama: {status_saat_ini}) [Kosongkan untuk batal]: ").upper().strip()
                
                if not status_input:
                    print("Perubahan Status Unit dibatalkan.")
                    break
                    
                if status_input == "TERSEDIA" or status_input == "DISEWA":
                    status_baru = status_input.title()
                    
                    konfirm_simpan = input(f"Yakin ingin mengubah Status Unit menjadi '{status_baru}'? (Y/N): ").upper()
                    if konfirm_simpan == "Y":
                        mobil[plat_ubah][2] = status_baru
                        ubah = True
                        print(f"Status Unit berhasil diubah menjadi: {status_baru}")
                    break
                else:
                    print("Status Unit harus diisi 'Tersedia' atau 'Disewa'.")
        else:
            print("Pilihan tidak valid.")
            
    if ubah:
        print(f"\nData Mobil {plat_ubah} berhasil diupdate!")
        tampilkan_daftar()
    else:
        print("Tidak ada perubahan yang dilakukan.")

# function untuk menghapus data mobil
def hapus_mobil():
    
    global mobil
    if not mobil:
        print("Database mobil kosong, tidak ada data untuk dihapus.")
        return

    tampilkan_daftar() 
    
    while True:
        plat_hapus = input("Masukkan Plat TNKB yang ingin dihapus (atau ketik 'Batal' untuk batal) : ").upper().strip().replace(' ', '')

        if plat_hapus == 'BATAL':
            print("\nHapus data dibatalkan.")
            return

        if plat_hapus in mobil:
            break
        else:
            print(f"Plat TNKB '{plat_hapus}' tidak ditemukan! Silakan coba lagi atau ketik 'Batal' untuk batal.")

    data_lama = mobil[plat_hapus]
    nama_lama_awal = data_lama[0]
    harga_lama_awal = data_lama[1]
    status_lama_awal = data_lama[2]
    
    print(f"\n--- DATA MOBIL SAAT INI ({plat_hapus}) ---")
    print(f"1. Nama Mobil : {nama_lama_awal}") 
    print(f"2. Harga Sewa : Rp{harga_lama_awal:,.0f}")
    print(f"3. Status Unit : {status_lama_awal}")
    print("------------------------------------------")
    
    nama_kend = mobil[plat_hapus][0]
    konfirm = input(f"Yakin ingin menghapus {plat_hapus} {nama_kend} dari database? (Y/N): ").upper()

    if konfirm == "Y":
        del mobil[plat_hapus]
        print(f"\nData Mobil {nama_kend} dengan Plat TNKB {plat_hapus} berhasil dihapus.")
        tampilkan_daftar()
    else:
        print("\nHapus data dibatalkan.")

# function untuk menjalankan program
def prog_rental():
    while True:
        pilih_menu = tampilkan_menu()

        if pilih_menu == "1":
            menu_tampilkan_data()
        elif pilih_menu == "2":
            tambah_mobil()
        elif pilih_menu == "3":
            ubah_mobil()
        elif pilih_menu == "4":
            hapus_mobil()
        elif pilih_menu == "5":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Menu tidak valid, coba lagi.")

prog_rental()