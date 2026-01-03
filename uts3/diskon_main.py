from diskon_utlis import parse_daftar_harga, hitung_total_belanja, hitung_potongan_diskon

data_harga = input("Masukkan daftar harga barang : ")
daftar_harga = parse_daftar_harga(data_harga)
total_sebelum_diskon = hitung_total_belanja(daftar_harga)
potongan = hitung_potongan_diskon(total_sebelum_diskon)
total_bayar_akhir = total_sebelum_diskon - potongan

print("Total harga sebelum diskon : Rp", total_sebelum_diskon)
print("Potongan diskon            : Rp", potongan)
print("Total yang harus dibayar   : Rp", total_bayar_akhir)
