#Konstruksi Dasar Python

#Sequential : Eksekusi perintah secara berurutan
print("BELAJAR MENGGUNAKAN KODE SECARA SEQUENTIAL")
import datetime
print("Halo Indonesia")
print("By Ragowo")
print("Tanggal :", datetime.datetime.now())
print("-" * 39)
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

# Pengulangan
print("BELAJAR MENGGUNAKAN FOR")
anak = 3
for index_anak in range(1,anak+1): #jumlah pengulangan = 4-1 = 3
    print(f'Anak Ke #{index_anak}')
print("-" * 39)
print()

#Tipe Data Skalar ==> Tipe Data Sederhana
a1 = "Dina"
a2 = "Antok"
a3 = "Toyi"
print("Data semua anak:")
print(a1)
print(a2)
print(a3)
print()

# tipe data list / array
anak = ['Dina','Antok','Toyi']
print("Nama Semua Anak: ", anak)
print("Nama anak ke 2", f'Hai {anak[1]}')

print('Sapa Semua (dengan cara simpel)')
for a in anak:
    print(f'Hai {a}')

print('Sapa Semua (dengan cara ribet)')
for a in range(len(anak)):
    print(f'{a+1}. Hai {anak[a]}')



