# Konstruksi Dasar Python

# Sequential : Eksekusi perintah secara berurutan
print("BELAJAR MENGGUNAKAN KODE SECARA SEQUENTIAL")
import datetime

print("Halo Indonesia")
print("By Ragowo")
print("Tanggal :", datetime.datetime.now())
print("-" * 39)
print()
print()

# Pencabangan : Eksekusi sesuai dengan kondisi / syarat yang ditentukan
print("BELAJAR MENGGUNAKAN IF")
cepat = True
if cepat:
    print("Pakai Motor Sport")
else:
    print("Pakai Speda Brompton")
print("-" * 39)
print()
print()

# Pengulangan
print("BELAJAR MENGGUNAKAN FOR")
anak = 3
for index_anak in range(1, anak + 1):  # jumlah pengulangan = 4-1 = 3
    print(f'Anak Ke #{index_anak}')
print("-" * 39)
print()
print()

# Tipe Data Skalar ==> Tipe Data
print("BELAJAR MENGGUNAKAN TIPE DATA SKALAR")
a1 = "Dina"
a2 = "Antok"
a3 = "Toyi"
print("Data semua anak:")
print(a1)
print(a2)
print(a3)
print("-" * 39)
print()
print()

# tipe data list / array
print("BELAJAR MENGGUNAKAN TIPE DATA LIST")
anak = ['Dina', 'Antok', 'Toyi']
print("Nama Semua Anak: ", anak)
print("Nama anak ke 2", f'Hai {anak[1]}')

print('Sapa Semua (dengan cara simpel)')
for a in anak:
    print(f'Hai {a}')

print('Sapa Semua (dengan cara ribet)')
for a in range(len(anak)):
    print(f'{a + 1}. Hai {anak[a]}')
print("-" * 39)
print()
print()

# Tipe Data Dictionary : Menghubungkan antara Key dan Value
print("BELAJAR MENGGUNAKAN TIPE DATA DICTIONARY")
kamus_id_en = {'ayah': 'father', 'suami': 'husband', 'ibu': 'mother', 'istri': 'wife', 'anak laki-laki': 'son',
               'anak perempuan': 'daughter'}
print(kamus_id_en)
print(kamus_id_en['ayah'])
print()

print('Data ini dikirimkan dari Server OJOL, untuk memberikan info driver yang dekat user')
data_dari_server = {'tanggal': datetime.datetime.now(),'driver_list':[{'nama':'eko','jarak':'10m'},{'nama':'dwi','jarak':'20m'},{'nama':'tri','jarak':'30m'}]}

print(data_dari_server)
print(f"Driver yang dekat dengan user {data_dari_server['driver_list']}")
print(f"Driver yang paling jauh dengan user {data_dari_server['driver_list'][2]}")
print(f"Driver yang paling dekat dengan user jaraknya {data_dari_server['driver_list'][0]['jarak']}")
