def hitung_total_pembayaran(list_harga):
    total = sum(list_harga)
    return total

def ambil_input_harga(no_konsumen):
    input_str = input(f"Masukkan Harga Barang yang dibeli Konsumen {no_konsumen}: ")
    
    # Konversi input string ke list integer
    list_harga = list(map(int, input_str.split()))
    return list_harga
