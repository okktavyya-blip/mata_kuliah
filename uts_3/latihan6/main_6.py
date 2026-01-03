from utliss_6 import parse_daftar_harga, hitung_total_belanja, hitung_pajak

data_harga = input("Masukkan daftar harga barang : ")
daftar_harga = parse_daftar_harga(data_harga)
total_belanja = hitung_total_belanja(daftar_harga)
pajak = hitung_pajak(total_belanja)
total_bayar_akhir = total_belanja + pajak

print("Total harga barang         : Rp", total_belanja)
print("Pajak (10%)                : Rp", pajak)
print("Total yang harus dibayar   : Rp", total_bayar_akhir)
