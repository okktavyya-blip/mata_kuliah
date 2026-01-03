import math

def persegi(sisi):
    keliling = 4 * sisi
    luas = sisi ** 2
    return keliling, luas

def persegi_panjang(panjang, lebar):
    keliling = 2 * (panjang + lebar)
    luas = panjang * lebar
    return keliling, luas

def segitiga(sisi_a, sisi_b, sisi_c, tinggi):
    keliling = sisi_a + sisi_b + sisi_c
    luas = 0.5 * sisi_a * tinggi
    return keliling, luas

def jajar_genjang(alas, sisi_miring, tinggi):
    keliling = 2 * (alas + sisi_miring)
    luas = alas * tinggi
    return keliling, luas

def layang_layang(diag1, diag2, sisi1, sisi2):
    keliling = 2 * (sisi1 + sisi2)
    luas = 0.5 * diag1 * diag2
    return keliling, luas

def belah_ketupat(diag1, diag2, sisi):
    keliling = 4 * sisi
    luas = 0.5 * diag1 * diag2
    return keliling, luas

def trapesium(sisi_atas, sisi_bawah, sisi_miring1, sisi_miring2, tinggi):
    keliling = sisi_atas + sisi_bawah + sisi_miring1 + sisi_miring2
    luas = 0.5 * (sisi_atas + sisi_bawah) * tinggi
    return keliling, luas

def lingkaran(jari_jari):
    keliling = 2 * math.pi * jari_jari
    luas = math.pi * (jari_jari ** 2)
    return keliling, luas

def heksagon(sisi):
    keliling = 6 * sisi
    luas = (3 * math.sqrt(3) / 2) * (sisi ** 2)
    return keliling, luas

def pentagon(sisi):
    tinggi_segitiga = (sisi * math.sqrt(3)) / 2
    keliling = 5 * sisi
    luas = (5 * sisi * tinggi_segitiga) / 2
    return keliling, luas

def bersihkan_layar():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_menu():
    bersihkan_layar()
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Jajar Genjang")
    print("5. Layang-layang")
    print("6. Belah Ketupat")
    print("7. Trapesium")
    print("8. Lingkaran")
    print("9. Heksagon")
    print("10. Pentagon")
    print("11. Keluar")

def validasi_pilihan(pilihan):
    try:
        pilihan_int = int(pilihan)
        return pilihan_int in [1,2,3,4,5,6,7,8,9,10,11], pilihan_int
    except ValueError:
        return False, None