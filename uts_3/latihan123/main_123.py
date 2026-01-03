from utlis_123 import cari_nilai_terbesar, cari_nilai_terkecil, parse_list, hitung_total_penjumlahan, nilai_kelulusan, cek_kelulusan

data = input("Masukkan data: ")

data = parse_list(data)

nilai_terbesar = cari_nilai_terbesar(data)
nilai_terkecil = cari_nilai_terkecil(data)
total_penjumlahan = hitung_total_penjumlahan(data)
rata_rata = nilai_kelulusan(data)
status_kelulusan = cek_kelulusan(rata_rata)

print("Nilai terbesar: ", nilai_terbesar)
print("nilai terkecil :", nilai_terkecil)
print("Total penjumlahan: ", total_penjumlahan)
print("Nilai rata-rata: ", rata_rata)
print("Status kelulusan: ", status_kelulusan)
