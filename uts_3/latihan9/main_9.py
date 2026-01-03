from utlis_9 import hitung_rata_rata, ambil_input_nilai

def main():
    jumlah_mahasiswa = int(input("Masukkan Jumlah Mahasiswa: "))
    
    for i in range(1, jumlah_mahasiswa + 1):
        list_nilai = ambil_input_nilai(i)
        rata = hitung_rata_rata(list_nilai)
        print(f"Rata - Rata Nilai Mahasiswa {i}: {rata}")

if __name__ == "__main__":
    main()
