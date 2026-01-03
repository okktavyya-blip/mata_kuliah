from utlis_8 import *

def main():
    # Input jumlah konsumen
    jumlah_konsumen = int(input("Masukkan Jumlah Konsumen: "))
    
    # Proses setiap konsumen
    for i in range(1, jumlah_konsumen + 1):
        list_harga = ambil_input_harga(i)
        total = hitung_total_pembayaran(list_harga)
        print(f"Total Pembayaran Konsumen {i}: {total}")

if __name__ == "__main__":
    main()
