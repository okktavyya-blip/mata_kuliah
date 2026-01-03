from utliss_7 import konversi_ke_float, atur_desimal

input_angka = input("Masukkan angka desimal : ")
banyak_koma = int(input("Masukkan jumlah angka di belakang koma: "))

angka_olah = konversi_ke_float(input_angka)
hasil_format = atur_desimal(angka_olah, banyak_koma)

print("Hasil konversi:", hasil_format)
