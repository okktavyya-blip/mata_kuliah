def parse_list(list_string):
    list_string = list_string.replace(" ", "")
    return list(map(int, list_string.split(",")))

def cari_nilai_terbesar(data):
    return max(data)   

def cari_nilai_terkecil(data):
    return min(data)		

def hitung_total_penjumlahan(data):
    return sum(data)

def nilai_kelulusan(data):
    return sum(data) / len(data)

def cek_kelulusan(nilai_rata_rata):
    if nilai_rata_rata >= 70:
        return "LULUS"
    else:
        return "TIDAK LULUS"
