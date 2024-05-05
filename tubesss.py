
# Membuat Variabel
nama_pemesan = []
kode_kereta = []
rute_kereta = []
kode_kelas = []
nama_kelas = []
harga = []

# Pengkondisian dan perulangan
jumlah_pesanan = int(input("Masukkan jumlah pesanan tiket : "))
list = [
    {"Kode": "|SRM|", "Rute": "Surabaya-Malang"},
    {"Kode": "|SRJ|", "Rute": "Surabaya-Jogja"},
]

from tabulate import tabulate

print(tabulate(list, headers="keys", tablefmt="grid"))

for i in range(jumlah_pesanan):
    print("Pesanan ke-", i + 1)
    nama_pemesan.append(input(" Masukkan nama pemesan : "))
    kode_kereta.append(input("Masukkan kode kereta |SRM|SRJ| : "))
    kode_kelas.append(input("Masukkan kode kelas |E|B|P| :"))
    if kode_kereta[i] == "SRM" or kode_kereta[i] == "srm":
        rute_kereta.append("Surabaya-Malang")
        if kode_kelas[i] == "E" or kode_kelas[i] == "e":
            nama_kelas.append("Ekonomi")
            harga.append(int(30000))
        elif kode_kelas[i] == "B" or kode_kelas[i] == "b":
            nama_kelas.append("Bisnis")
            harga.append(int(65000))
        elif kode_kelas[i] == "P" or kode_kelas[i] == "p":
            nama_kelas.append("Premium")
            harga.append(int(105000))
        else:
            nama_kelas.append("kosong")
            harga.append(int(0))

    elif kode_kereta[i] == "SRJ" or kode_kereta[i] == "srj":
        rute_kereta.append("Surabaya-Jogja")
        if kode_kelas[i] == "E" or kode_kelas[i] == "e":
            nama_kelas.append("Ekonomi")
            harga.append(int(70000))
        elif kode_kelas[i] == "B" or kode_kelas[i] == "b":
            nama_kelas.append("Bisnis")
            harga.append(int(125000))
        elif kode_kelas[i] == "P" or kode_kelas[i] == "p":
            nama_kelas.append("Bisnis")
            harga.append(int(175000))
        else:
            nama_kelas.append("kosong")
            harga.append(int(0))
    else:
        rute_kereta.append("Tidak ada")
        if kode_kelas[i] == "E" or kode_kelas[i] == "e":
            nama_kelas.append("Ekonomi")
            harga.append(int(0))
        elif kode_kelas[i] == "B" or kode_kelas[i] == "b":
            nama_kelas.append("Bisnis")
            harga.append(int(0))
        elif kode_kelas[i] == "P" or kode_kelas[i] == "p":
            nama_kelas.append("Bisnis")
            harga.append(int(0))
        else:
            nama_kelas.append("kosong")
            harga.append(int(0))

# Perhitungan
total = sum(harga)
if total > 200000:
    diskon = 10 / 100 * total
else:
    diskon = 0

bayar = total - diskon

# Output / keluaran
import pandas as pd

data = {
    "Nama": nama_pemesan,
    "Kereta": rute_kereta,
    "Kelas": nama_kelas,
    "Harga": harga,
}
rekap_data = pd.DataFrame(data)
print("=" * 50)
print("\tprogram Pemesanan Tiket Kereta Api")
print("=" * 50)
print(rekap_data)
print("=" * 50)
print("Total Pemesanan\t=", total)
print("Diskon\t=", diskon)
print("Total Bayar\t=", bayar)
uang_bayar = int(input("Masukkan Uang: "))
kembalian = uang_bayar - bayar
print("Kembalian\t:", kembalian)
print("=" * 50)


