from utlis import *

if __name__ == "__main__":
    while True:
        tampilkan_menu()
        pilihan = input("Pilih bangun ruang: ").strip()
        
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
        
        lp, vol = None, None
        if pilihan_int == 1:
            r, t = float(input("Masukkan jari-jari: ")), float(input("Masukkan tinggi: "))
            lp, vol = tabung(r, t)
        elif pilihan_int == 2:
            r = float(input("Masukkan jari-jari: "))
            lp, vol = bola(r)
        elif pilihan_int == 3:
            sa, ta, tl = float(input("Masukkan sisi alas: ")), float(input("Masukkan tinggi alas: ")), float(input("Masukkan tinggi limas: "))
            lp, vol = limas_segilima(sa, ta, tl)
        elif pilihan_int == 4:
            p, l, t = float(input("Masukkan panjang: ")), float(input("Masukkan lebar: ")), float(input("Masukkan tinggi: "))
            lp, vol = balok(p, l, t)
        elif pilihan_int == 5:
            sa, ta, tl = float(input("Masukkan sisi alas: ")), float(input("Masukkan tinggi alas: ")), float(input("Masukkan tinggi limas: "))
            lp, vol = limas(sa, ta, tl)
        elif pilihan_int == 6:
            sa, tl = float(input("Masukkan sisi alas: ")), float(input("Masukkan tinggi limas: "))
            lp, vol = limas_segiempat(sa, tl)
        elif pilihan_int == 7:
            s = float(input("Masukkan sisi: "))
            lp, vol = kubus(s)
        elif pilihan_int == 8:
            d1, d2, tl = float(input("Masukkan diagonal 1 alas: ")), float(input("Masukkan diagonal 2 alas: ")), float(input("Masukkan tinggi limas: "))
            lp, vol = limas_belah_ketupat(d1, d2, tl)
        elif pilihan_int == 9:
            sa, sb, ta, tl = float(input("Masukkan sisi atas: ")), float(input("Masukkan sisi bawah: ")), float(input("Masukkan tinggi alas: ")), float(input("Masukkan tinggi limas: "))
            lp, vol = limas_trapesium(sa, sb, ta, tl)
        elif pilihan_int == 10:
            r, t = float(input("Masukkan jari-jari: ")), float(input("Masukkan tinggi: "))
            lp, vol = kerucut(r, t)
        
        print(f"Luas Permukaan: {lp:.2f}, Volume: {vol:.2f}")
        input("Tekan enter untuk kembali ke menu...")
