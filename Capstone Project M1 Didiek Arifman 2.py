from prettytable import PrettyTable

# ZUGOSHI STORE STOK DATABASE
# Part ini dikhususkan sebagai dummy Collection Data Type yang digunakan pada ZUGOSHI WAREHOUSE MANAGEMENT SYSTEM V2.0, 
# pada pengembangannya nanti data akan dibuat dalam bentuk.CSV agar lebih mudah untuk penginputannya.
stok_gudang = [
    {
        "StokID": "AF-001", "Nama Barang": "Strootrooper 1/12", "Kategori": "Action Figure", "Brand": "Bandai", 
        "Stok Awal": 50, "Masuk": 20, "Keluar": 10, "Satuan": "Pcs", 
        "Harga Beli": 350000, "Harga Jual": 550000,
        "Tgl Masuk": "10-01-2024", "Tgl Keluar": "15-01-2024", "Lokasi": "AC2R1",
        "Last Update": "15-01-2024"
    },
    {
        "StokID": "AF-002", "Nama Barang": "Luttfy One Piece 1/17", "Kategori": "Action Figure", "Brand": "Namco", 
        "Stok Awal": 23, "Masuk": 11, "Keluar": 7, "Satuan": "Pcs", 
        "Harga Beli": 375000, "Harga Jual": 850000,
        "Tgl Masuk": "10-01-2024", "Tgl Keluar": "19-01-2024", "Lokasi": "AC2R1",
        "Last Update": "15-01-2024"
    },
    {
        "StokID": "DC-001", "Nama Barang": "HW 1/64 Porche 911 2001", "Kategori": "Diecast", "Brand": "Hotwheels", 
        "Stok Awal": 10, "Masuk": 5, "Keluar": 2, "Satuan": "Pcs", 
        "Harga Beli": 80000, "Harga Jual": 95000,
        "Tgl Masuk": "11-01-2024", "Tgl Keluar": "16-01-2024", "Lokasi": "BC1R2",
        "Last Update": "16-01-2024"
    },
    {
        "StokID": "DC-002", "Nama Barang": "MA 1/12 Porche 911 1998", "Kategori": "Diecast", "Brand": "Stonemaier", 
        "Stok Awal": 1, "Masuk": 0, "Keluar": 0, "Satuan": "Pcs", 
        "Harga Beli": 1525000, "Harga Jual": 3500000,
        "Tgl Masuk": "11-01-2024", "Tgl Keluar": "", "Lokasi": "BC3R2",
        "Last Update": "18-01-2024"
    },
    {
         "StokID": "BG-002", "Nama Barang": "Snake and Ladder Deluxe", "Kategori": "Boardgame", "Brand": "Model Art", 
        "Stok Awal": 1, "Masuk": 0, "Keluar": 1, "Satuan": "Pcs", 
        "Harga Beli": 625000, "Harga Jual": 975000,
        "Tgl Masuk": "11-01-2024", "Tgl Keluar": "18-01-2024", "Lokasi": "CC13R2",
        "Last Update": "18-01-2024"
    },
    {
        "StokID": "DC-003", "Nama Barang": "HW 1/64 Box E 2012", "Kategori": "Diecast", "Brand": "Hotwheels", 
        "Stok Awal": 11, "Masuk": 1, "Keluar": 1, "Satuan": "Box", 
        "Harga Beli": 80000, "Harga Jual": 95000,
        "Tgl Masuk": "11-01-2024", "Tgl Keluar": "16-01-2024", "Lokasi": "BC1R2",
        "Last Update": "16-01-2024"
    }
]

# CALCULATION FUNCTION
# Part ini digunakan sebagai penyimpanan fungsi kalkulasi dan konversi yang digunakan 
# dalam ZUGOSHI WAREHOUSE MANAGEMENT SYSTEM V2.0
def hitung_stok_akhir(barang):
    return int(barang["Stok Awal"]) + int(barang["Masuk"]) - int(barang["Keluar"])

def format_rupiah(angka):
    return f"Rp {angka:,}"

def konversi_ke_update(tgl_str):
    """Mengubah DD-MM-YYYY ke YYYYMMDD untuk perbandingan kronologis"""
    if not tgl_str or tgl_str == "-" or tgl_str == "":
        return "00000000"
    bagian = tgl_str.split("-")
    if len(bagian) == 3:
        # Format: YYYY + MM + DD
        return bagian[2] + bagian[1] + bagian[0]
    return "00000000"

# SORTING FUNCTION
# Part ini digunakan sebagai penyimpanan fungsi sorting barang berdasarkan kolom.

def ambil_stok_id(barang): return barang["StokID"]
def ambil_nama_barang(barang): return barang["Nama Barang"]
def ambil_kategori(barang): return barang["Kategori"]
def ambil_stok_akhir(barang): return hitung_stok_akhir(barang)
def ambil_last_update(barang): return konversi_ke_update(barang["Last Update"])
def ambil_terjual(barang): return barang["Keluar"]

# TABLE DISPLAY FUNCTION
# Part ini merupakan fungsi yang digunakan untuk mengedit tabel. Tabel yang dipakai memakai plugin Prettytable agar terlihat lebih rapih.

def tampilkan_tabel(data_filter=None):
    tabel = PrettyTable()
    tabel.field_names = ["StokID", "Nama Barang", "Brand", "Kategori", "Stok Awal", "Satuan", "Masuk", "Terjual", "Stok Akhir", "Harga Beli", "Harga Jual", "Lokasi", "Last Update"]
    
    sumber_data = data_filter if data_filter is not None else stok_gudang
    
    for barang in sumber_data:
        tabel.add_row([
            barang["StokID"], 
            barang["Nama Barang"], 
            barang["Brand"],
            barang["Kategori"],
            barang["Stok Awal"],
            barang["Satuan"],
            barang["Masuk"],
            barang["Keluar"],
            hitung_stok_akhir(barang), 
            format_rupiah(barang["Harga Beli"]),
            format_rupiah(barang["Harga Jual"]),
            barang["Lokasi"],
            barang["Last Update"]
        ])
    tabel.align["Nama Barang"] = "l"
    print(tabel)

# NAVIGATION FUNCTION
# Part ini merupakan penyimpanan fungsi navigasi pencarian stok barang

def menu_laporan():
    print("\n>>> OPSI PENGURUTAN LAPORAN")
    print("1. Stok ID (Default) | 2. Nama Barang | 3. Kategori | 4. Stok Akhir | 5. Tanggal Update")
    pilih = input("Pilih kriteria (1-5): ")

    print("\n1. Ascending (A-Z / Kecil-Besar) | 2. Descending (Z-A / Besar-Kecil)")
    metode = input("Pilih metode (1-2): ")
    is_reverse = (metode == "2")

    sort_keys = {
        "1": ambil_stok_id,
        "2": ambil_nama_barang,
        "3": ambil_kategori,
        "4": ambil_stok_akhir,
        "5": ambil_last_update
    }

    key_func = sort_keys.get(pilih, ambil_stok_id)
    data_urut = sorted(stok_gudang, key=key_func, reverse=is_reverse)

    print("\n>>> STOK BARANG ZUGOSHI STORE:")
    tampilkan_tabel(data_urut)

def menu_cari_barang():
    print("\n" + "="*45)
    keyword = input("Masukkan Nama Barang atau StokID:").lower()
    hasil_cari = [b for b in stok_gudang if keyword in b["Nama Barang"].lower() or keyword in b["StokID"].lower()]
    
    if hasil_cari:
        print(f"\n>>> Ditemukan {len(hasil_cari)} barang dengan kata kunci '{keyword}':")
        tampilkan_tabel(hasil_cari)
    else:
        print(f"\n[!] Barang dengan kata kunci '{keyword}' tidak ditemukan.")
    print("="*90)

# MENU UTAMA

def main_menu():
    lebar = 100
    while True:
        print("\n" + "#" * lebar)
        print("ZUGOSHI WAREHOUSE MANAGEMENT SYSTEM V2.0".center(lebar))
        print("#" * lebar)
        print("1. Laporan Stok (Pilihan Sortir)")
        print("2. Update Stok & Harga (Tambah ID Baru / Jual / Ubah Harga)")
        print("3. Stok Favorit (Top 3 Terlaris)")
        print("4. Stok Tidak Favorit (Kurang Laku)")
        print("5. Cari Barang (Berdasarkan Nama/StokID)")
        print("6. Keluar")
        print("=" * lebar)
        
        pilihan = input("Pilih menu: ")

        if pilihan == "1": #FITUR READ pilihan menu ini akan menampilkan opsi membaca laporan sesuai kebutuhan user.
            menu_laporan()
            input("\nTekan Enter untuk kembali...")
        
        elif pilihan == "2":
            sid = input("Masukkan StokID (Max 6 Char): ").upper()
            if len(sid) > 6:
                print("StokID maksimal 6 karakter!"); continue
            
            barang = next((item for item in stok_gudang if item["StokID"] == sid), None)

            try:
                print("\n1. Tambah Stok | 2. Jual Barang | 3. Update Harga")
                sub = input("Pilih aksi: ")
                
                # FITUR TAMBAH STOK
                if sub == "1":
                    if barang:
                        jml = int(input(f"Tambah stok '{barang['Nama Barang']}': "))
                        tgl = input(f"Tanggal (DD-MM-YYYY) [Min {barang['Last Update']}]: ")
                        if konversi_ke_update(tgl) < konversi_ke_update(barang["Last Update"]):
                            print("Tanggal yang Anda masukan SALAH!")
                        else:
                            barang["Masuk"] += jml
                            barang["Last Update"] = tgl
                            print("Stok berhasil ditambah."); tampilkan_tabel([barang])
                    else:
                        print("\n[ StokID Baru Terdeteksi - Registrasi Barang Baru ]")
                        nama = input("Nama Barang: ")
                        kat = input("Kategori (Max 15 Char): ")
                        if len(kat) > 15: print("GAGAL: Kategori Max 15 karakter!"); continue
                        
                        p_brand = input("Nama Brand : ")
                        stok_awal = int(input("Stok Awal: "))
                        h_beli = int(input("Harga Beli: "))
                        h_jual = int(input("Harga Jual: "))
                        l_lokasi = input("Lokasi: ")
                        tgl_input = input("Tanggal Hari Ini (DD-MM-YYYY): ")
                        
                        barang_baru = {
                            "StokID": sid, "Nama Barang": nama, "Kategori": kat, "Brand": p_brand, 
                            "Stok Awal": stok_awal, "Masuk": 0, "Keluar": 0, "Satuan": "Pcs", 
                            "Harga Beli": h_beli, "Harga Jual": h_jual,
                            "Tgl Masuk": tgl_input, "Tgl Keluar": "-", "Lokasi": l_lokasi,"Last Update": tgl_input
                        }
                        stok_gudang.append(barang_baru)
                        print("Barang Baru Berhasil Didaftarkan!"); tampilkan_tabel([barang_baru])

                # FITUR DELETE STOK
                elif sub == "2":
                    if not barang: print("Maaf barang belum terdaftar!"); continue
                    sisa = hitung_stok_akhir(barang)
                    jml = int(input(f"Jumlah Terjual (Tersedia {sisa}): "))
                    if jml > sisa:
                        print("Maaf stok tidak mencukupi!")
                    else:
                        tgl = input(f"Tanggal Jual (DD-MM-YYYY) [Min {barang['Last Update']}]: ")
                        if konversi_ke_update(tgl) < konversi_ke_update(barang["Last Update"]):
                            print("Tanggal yang Anda masukan SALAH!")
                        else:
                            barang["Keluar"] += jml
                            barang["Last Update"] = tgl
                            print("Penjualan Berhasil."); tampilkan_tabel([barang])

                # FITUR UPDATE
                elif sub == "3":
                    if not barang: print("Barang belum terdaftar!"); continue
                    print(f"\nHarga Saat Ini -> Beli: {format_rupiah(barang['Harga Beli'])} | Jual: {format_rupiah(barang['Harga Jual'])}")
                    h_beli_baru = int(input("Harga Beli Baru: "))
                    h_jual_baru = int(input("Harga Jual Baru: "))
                    tgl = input(f"Tanggal Perubahan (DD-MM-YYYY) [Min {barang['Last Update']}]: ")
                    
                    if konversi_ke_update(tgl) < konversi_ke_update(barang["Last Update"]):
                        print("Tanggal tidak boleh mundur!")
                    else:
                        barang["Harga Beli"] = h_beli_baru
                        barang["Harga Jual"] = h_jual_baru
                        barang["Last Update"] = tgl
                        print("Harga Berhasil Diperbarui!"); tampilkan_tabel([barang])
                
                else:
                    print("Pilihan sub-menu tidak tersedia.")

            except ValueError:
                print("Input salah! Pastikan memasukkan angka untuk stok dan harga.")

        elif pilihan == "3": #FITUR READ
            print("\n>>> TOP 3 STOK FAVORIT (PALING LAKU)")
            data_fav = sorted(stok_gudang, key=ambil_terjual, reverse=True)
            tampilkan_tabel(data_fav[:3])

        elif pilihan == "4": #FITUR READ
            print("\n>>> TOP 3 STOK TIDAK FAVORIT (KURANG LAKU)")
            data_unfav = sorted(stok_gudang, key=ambil_terjual)
            tampilkan_tabel(data_unfav[:3])

        elif pilihan == "5": #FITUR SEARCH
            menu_cari_barang()
            input("\nTekan Enter untuk kembali...")

        elif pilihan == "6":
            print("Terima kasih telah menggunakan ZUGOSHI WAREHOUSE MANAGEMENT SYSTEM V2.0. Sampai jumpa!")
            break

if __name__ == "__main__":
    main_menu()