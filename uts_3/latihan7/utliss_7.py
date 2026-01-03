def konversi_ke_float(teks_angka):
    return float(teks_angka.replace(".", ",").replace(",", ".", 1))

def atur_desimal(angka, jumlah_desimal):
    return "{0:.{1}f}".format(angka, jumlah_desimal).replace(".", ",")
