from utliss import *

if __name__ == "__main__":
    while True:
        tampilkan_menu()
        pilihan = input("Pilih bangun datar: ").strip()
        
        if not pilihan:
            continue
        
        valid, pilihan_int = validasi_pilihan(pilihan)
        if not valid:
            print("Pilihan tidak valid! Masukkan angka yang terdaftar.")
            input("Tekan enter untuk kembali...")
            continue
        
        if pilihan_int == 11:
            print("Keluar dari program...")
            break
        
        k, l = None, None
        if pilihan_int == 1:
            s = float(input("Masukkan sisi: "))
            k, l = persegi(s)
        elif pilihan_int == 2:
            p = float(input("Masukkan panjang: "))
            lb = float(input("Masukkan lebar: "))
            k, l = persegi_panjang(p, lb)
        elif pilihan_int == 3:
            a = float(input("Masukkan sisi a: "))
            b = float(input("Masukkan sisi b: "))
            c = float(input("Masukkan sisi c: "))
            t = float(input("Masukkan tinggi: "))
            k, l = segitiga(a, b, c, t)
        elif pilihan_int == 4:
            a = float(input("Masukkan alas: "))
            sm = float(input("Masukkan sisi miring: "))
            t = float(input("Masukkan tinggi: "))
            k, l = jajar_genjang(a, sm, t)
        elif pilihan_int == 5:
            d1 = float(input("Masukkan diagonal 1: "))
            d2 = float(input("Masukkan diagonal 2: "))
            s1 = float(input("Masukkan sisi 1: "))
            s2 = float(input("Masukkan sisi 2: "))
            k, l = layang_layang(d1, d2, s1, s2)
        elif pilihan_int == 6:
            d1 = float(input("Masukkan diagonal 1: "))
            d2 = float(input("Masukkan diagonal 2: "))
            s = float(input("Masukkan sisi: "))
            k, l = belah_ketupat(d1, d2, s)
        elif pilihan_int == 7:
            sa = float(input("Masukkan sisi atas: "))
            sb = float(input("Masukkan sisi bawah: "))
            sm1 = float(input("Masukkan sisi miring 1: "))
            sm2 = float(input("Masukkan sisi miring 2: "))
            t = float(input("Masukkan tinggi: "))
            k, l = trapesium(sa, sb, sm1, sm2, t)
        elif pilihan_int == 8:
            r = float(input("Masukkan jari-jari: "))
            k, l = lingkaran(r)
        elif pilihan_int == 9:
            s = float(input("Masukkan sisi: "))
            k, l = heksagon(s)
        elif pilihan_int == 10:
            s = float(input("Masukkan sisi: "))
            k, l = pentagon(s)
        
        print(f"Keliling: {k:.2f}, Luas: {l:.2f}")
        input("Tekan enter untuk kembali ke menu...")
