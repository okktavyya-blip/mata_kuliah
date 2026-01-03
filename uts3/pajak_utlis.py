def parse_daftar_harga(input_string):
    input_string = input_string.replace(" ", "")
    return list(map(int, input_string.split(",")))

def hitung_total_belanja(daftar_harga):
    return sum(daftar_harga)

def hitung_pajak(total_belanja):
    return total_belanja * 0.10  # Pajak 10%
