def hitung_rata_rata(list_nilai):
    rata = sum(list_nilai) / len(list_nilai)
    return rata

def ambil_input_nilai(no_mahasiswa):
    input_str = input(f"Masukkan Nilai Mahasiswa {no_mahasiswa}: ")
    list_nilai = list(map(int, input_str.split()))
    return list_nilai
