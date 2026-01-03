from utlis import *


def proses_perhitungan(pilihan_int):
    if pilihan_int == 11:
        print("Keluar dari program...")
        return None, None, True  # (luas permukaan, volume, status_keluar)
    
    lp, vol = None, None
    if pilihan_int == 1:
        r = float(input("Masukkan jari-jari: "))
        t = float(input("Masukkan tinggi: "))
        lp, vol = tabung(r, t)
    elif pilihan_int == 2:
        r = float(input("Masukkan jari-jari: "))
        lp, vol = bola(r)
    elif pilihan_int == 3:
        sa = float(input("Masukkan sisi alas: "))
        ta = float(input("Masukkan tinggi alas: "))
        tl = float(input("Masukkan tinggi limas: "))
        lp, vol = limas_segilima(sa, ta, tl)
    elif pilihan_int == 4:
        p = float(input("Masukkan panjang: "))
        l = float(input("Masukkan lebar: "))
        t = float(input("Masukkan tinggi: "))
        lp, vol = balok(p, l, t)
    elif pilihan_int == 5:
        sa = float(input("Masukkan sisi alas: "))
        ta = float(input("Masukkan tinggi alas: "))
        tl = float(input("Masukkan tinggi limas: "))
        lp, vol = limas(sa, ta, tl)
    elif pilihan_int == 6:
        sa = float(input("Masukkan sisi alas: "))
        tl = float(input("Masukkan tinggi limas: "))
        lp, vol = limas_segiempat(sa, tl)
    elif pilihan_int == 7:
        s = float(input("Masukkan sisi: "))
        lp, vol = kubus(s)
    elif pilihan_int == 8:
        d1 = float(input("Masukkan diagonal 1 alas: "))
        d2 = float(input("Masukkan diagonal 2 alas: "))
        tl = float(input("Masukkan tinggi limas: "))
        lp, vol = limas_belah_ketupat(d1, d2, tl)
    elif pilihan_int == 9:
        sa = float(input("Masukkan sisi atas: "))
        sb = float(input("Masukkan sisi bawah: "))
        ta = float(input("Masukkan tinggi alas: "))
        tl = float(input("Masukkan tinggi limas: "))
        lp, vol = limas_trapesium(sa, sb, ta, tl)
    elif pilihan_int == 10:
        r = float(input("Masukkan jari-jari: "))
        t = float(input("Masukkan tinggi: "))
        lp, vol = kerucut(r, t)
    
    return lp, vol, False


# Blok utama dipindahkan ke akhir
if __name__ == "__main__":
    while True:
        tampilkan_menu()
        pilihan = input("Pilih bangun ruang: ")
        
        if pilihan.strip() == "":
            continue
        
        valid, pilihan_int = validasi_pilihan(pilihan)
        if not valid:
            print("Pilihan tidak valid! Masukkan angka yang terdaftar.")
            input("Tekan enter untuk kembali...")
            continue
        
        lp, vol, keluar = proses_perhitungan(pilihan_int)
        if keluar:
            break
        
        print(f"Luas Permukaan: {lp:.2f}, Volume: {vol:.2f}")
        input("Tekan enter untuk kembali ke menu...")
