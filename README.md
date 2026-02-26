# Zugoshi-Warehouse-Management-System
Capstone Project Modul I Online Class Job Connector Data Science - Didiek Arifman - Case Study : Data Stock Gudang

CASE STUDY
Untuk Aplikasinya saya menggunakan Real Case dari Collectible Toys Store yang ada di ICE Business Park BSD Tangerang yang bernama Zugoshi Store. Zugoshi Storeberdiri sejak awal tahun 2020. Seiring berkembangnya usaha Zugoshi Store stok barang yang dijual pun semakin banyak dan menumpuk sehingga dibutuhkan suatu sistem manajemen untuk mengelola stok barang yang berada di gudang penyimpanan.

MASALAH UTAMA
•	Human Error: Salah catat stok, karena bergantung pada ingatan/kertas.
•	Ghost Inventory: Barang ada di data tapi tidak ada di rak (atau sebaliknya).
•	Deadstock: Barang menumpuk hingga rusak karena tidak terpantau.
•	Proses Picking yang Lama: Staf gudang berputar-putar mencari barang karena tata letak tidak terorganisir secara         sistematis.

SOLUSI
Aplikasi berbasis CLI (Command Line Interface) yang dirancang untuk mengelola inventaris barang secara akurat. Sistem ini mencakup pencatatan stok awal, penambahan stok, penjualan barang, hingga analisis barang terlaris.

•	Manajemen Inventaris: Mendukung pendaftaran barang baru dan pembaruan stok barang lama secara otomatis dalam satu menu.
•	Audit Trail (Last Update): Melacak tanggal terakhir setiap aset diubah untuk memastikan transparansi data.
•	Sortir Fleksibel: Laporan yang dapat diurutkan berdasarkan 5 kriteria berbeda dengan metode Ascending atau Descending.
•	Optimalisasi Ruang: Tata letak yang sistematis dan terorganisir akan menghemat banyak ruang.
•	Inventory Location : Staf gudang dapat dengan mudah menemukan lokasi barang.
•	Stock Analis: Dapat memantau stok keluar masuk barang dari gudang untuk menghindari Deadstock

FITUR
•	Stok Reporting : Mendapatkan informasi stok yang tesedia di gudang.
•	Stok Updating : Dapat mengupdate catatan stok yang tersedia di gudang.
•	Stok Analisis : Dapat menganalisa performa stok untuk membuat prediksi saat purchasing kedepannya.
•	Stok Searching : Mencari stok tertentu berdasarkan nama atau Stok ID
•	Low Stock : Mengetahui stok mana yang perlu ditambah.
•	Flexible Reporting : Laporan yang dapat diurutkan berdasarkan 5 kriteria berbeda dengan metode Ascending atau Descending.

STOK IDENTIFYING
Untuk mempermudah pencarian data maka setiap stok harus diberi identitas dan diklasifikasikan kedalam bentuk table database sesuai kebutuhan dari Zugoshi Store.

WORKFLOW APLIKASI
Main Menu
1. Laporan Stok (Pilihan Sortir)
    •	Laporan Stok Berdasarkan Stok ID
    •	Laporan Stok Berdasarkan Nama Barang
    •	Laporan Stok Berdasarkan Kategori
    •	Laporan Stok Berdasarkan Stok Akhir
    •	Laporan Stok Berdasarkan Tanggal Update
2. Update Stok & Harga (Tambah ID Baru / Jual / Ubah Harga)
    •	Menambah Stok Baru
      o	Input Stok ID Baru
      o	Input Nama Barang
      o	Input Kategori
      o	Input Brand
      o	Input Quantity
      o	Input Harga
      o	Input Tanggal
  •	Menambah Jumlah Stok yang Sudah Ada
      o	Input Stok ID
      o	Input Tambah Quantity
      o	Input Tanggal Update
  •	Mengurangi Jumlah Stok yang Sudah Ada
      o	Input StokID
      o	Input Kurang Quantity
      o	Input Tanggal Update
  •	Update Data Stok yang Sudah Ada
      o	Update Harga
      o	Update Tanggal
  •	Kembali ke Menu Utama
3. Stok Favorit (Top 3 Terlaris)
4. Stok Tidak Favorit (Kurang Laku)
5. Cari Barang (Berdasarkan Nama atau Stok ID)
    •	Input Nama Barang atau Stok ID
6. Keluar


