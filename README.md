# Pertemuan 1 Praktikum KB - Game Tebak Angka

### Mekanisme sederhanaya yaitu pemain diminta menebak angka rahasia yang dihasilkan acak oleh program dengan kesempatan tertentu.

### Konsep yang Digunakan
### 1. Struktur Kontrol
Program menggunakanstruktur kontrol yaitu:
while → untuk mengulang permainan selama kesempatan masih ada
if, elif, else → untuk mengecek hasil tebakan pemain

### 2. Struktur Data
Program menggunakan list untuk menyimpan riwayat tebakan pemain.
Contoh:
riwayat_tebakan = []
Setiap tebakan pemain akan disimpan menggunakan riwayat_tebakan.append(tebakan)

### 3. Library Python
Program menggunakan dua library bawaan Python:
- random, digunakan untuk menghasilkan angka acak.
contoh: random.randint(1, 25), berarti angka acaknya diantara 1 sampai 25

- time, digunakan untuk memberikan jeda sebelum menampilkan hasil.
contoh: time.sleep(1), berarti jeda selama 1detk


## Author
Rinaldi Dasa Bahtiar - H1D024065
Shift A Praktikum KB
