import math

def kubus(sisi):
    luas_permukaan = 6 * (sisi ** 2)
    volume = sisi ** 3
    return luas_permukaan, volume

def balok(panjang, lebar, tinggi):
    luas_permukaan = 2 * (panjang*lebar + panjang*tinggi + lebar*tinggi)
    volume = panjang * lebar * tinggi
    return luas_permukaan, volume

def limas(sisi_alas, tinggi_alas, tinggi_limas):
    luas_alas = 0.5 * sisi_alas * tinggi_alas
    luas_selimut = 4 * (0.5 * sisi_alas * math.sqrt((tinggi_limas**2) + (tinggi_alas/2)**2))
    luas_permukaan = luas_alas + luas_selimut
    volume = (1/3) * luas_alas * tinggi_limas
    return luas_permukaan, volume

def tabung(jari_jari, tinggi):
    luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)
    volume = math.pi * (jari_jari ** 2) * tinggi
    return luas_permukaan, volume

def bola(jari_jari):
    luas_permukaan = 4 * math.pi * (jari_jari ** 2)
    volume = (4/3) * math.pi * (jari_jari ** 3)
    return luas_permukaan, volume

def limas_segiempat(sisi_alas, tinggi_limas):
    luas_alas = sisi_alas ** 2
    luas_selimut = 2 * sisi_alas * math.sqrt((tinggi_limas**2) + (sisi_alas/2)**2)
    luas_permukaan = luas_alas + luas_selimut
    volume = (1/3) * luas_alas * tinggi_limas
    return luas_permukaan, volume

def limas_segilima(sisi_alas, tinggi_alas, tinggi_limas):
    luas_alas = (5 * sisi_alas * tinggi_alas) / 2
    luas_selimut = 5 * (0.5 * sisi_alas * math.sqrt((tinggi_limas**2) + (tinggi_alas/2)**2))
    luas_permukaan = luas_alas + luas_selimut
    volume = (1/3) * luas_alas * tinggi_limas
    return luas_permukaan, volume

def limas_belah_ketupat(diag1_alas, diag2_alas, tinggi_limas):
    luas_alas = 0.5 * diag1_alas * diag2_alas
    sisi_alas = math.sqrt((diag1_alas/2)**2 + (diag2_alas/2)**2)
    luas_selimut = 4 * (0.5 * sisi_alas * math.sqrt((tinggi_limas**2) + (sisi_alas/2)**2))
    luas_permukaan = luas_alas + luas_selimut
    volume = (1/3) * luas_alas * tinggi_limas
    return luas_permukaan, volume

def limas_trapesium(sisi_atas, sisi_bawah, tinggi_alas, tinggi_limas):
    luas_alas = 0.5 * (sisi_atas + sisi_bawah) * tinggi_alas
    sisi_miring_alas = math.sqrt(((sisi_bawah - sisi_atas)/2)**2 + tinggi_alas**2)
    luas_selimut = (sisi_atas + sisi_bawah + 2 * sisi_miring_alas) * math.sqrt((tinggi_limas**2) + (tinggi_alas/2)**2) / 2
    luas_permukaan = luas_alas + luas_selimut
    volume = (1/3) * luas_alas * tinggi_limas
    return luas_permukaan, volume

def kerucut(jari_jari, tinggi):
    garis_pelukis = math.sqrt(jari_jari**2 + tinggi**2)
    luas_permukaan = math.pi * jari_jari * (jari_jari + garis_pelukis)
    volume = (1/3) * math.pi * (jari_jari ** 2) * tinggi
    return luas_permukaan, volume

def prisma_segitiga(sisi_segitiga, tinggi_segitiga, tinggi_prisma):
    luas_alas = 0.5 * sisi_segitiga * tinggi_segitiga
    luas_permukaan = 2 * luas_alas + 3 * sisi_segitiga * tinggi_prisma
    volume = luas_alas * tinggi_prisma
    return luas_permukaan, volume

def bersihkan_layar():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_menu():
    bersihkan_layar()
    print("1. Tabung")
    print("2. Bola")
    print("3. Limas Segilima")
    print("4. Balok")
    print("5. Limas")
    print("6. Limas Segiempat")
    print("7. Kubus")
    print("8. Limas Belahketupat")
    print("9. Limas Trapesium")
    print("10. Kerucut")
    print("11. Keluar")

def validasi_pilihan(pilihan):
    try:
        pilihan_int = int(pilihan)
        return pilihan_int in [1,2,3,4,5,6,7,8,9, 10, 11], pilihan_int
    except ValueError:
        return False, None
