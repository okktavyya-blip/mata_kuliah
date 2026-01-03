def parse_daftar_harga(input_string):
    input_string = input_string.replace(" ", "")
    return list(map(int, input_string.split(",")))

def hitung_total_belanja(daftar_harga):
    return sum(daftar_harga)

def hitung_potongan_diskon(total_belanja):
    if total_belanja > 50000:
        return total_belanja * 0.01
    return 0
