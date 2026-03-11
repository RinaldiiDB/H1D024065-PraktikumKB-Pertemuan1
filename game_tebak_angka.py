import random
import time

print("=== GAME TEBAK ANGKA ===")
print("Tebak angka dari 1 sampai 25")
print()

angka_rahasia = random.randint(1, 25)
riwayat_tebakan = []
kesempatan = 5

while kesempatan > 0:
    tebakan = int(input("Masukkan tebakanmu: "))
    
    riwayat_tebakan.append(tebakan)
    print("Memeriksa jawaban...")
    time.sleep(1)
    if tebakan == angka_rahasia:
        print("Selamat tebakan kamu benar!")
        break
    elif tebakan < angka_rahasia:
        print("Angkanya terlalu kecil!")
    else:
        print("Angkanya terlalu besar!")
    kesempatan -= 1
    print("Sisa kesempatan:", kesempatan)
    print()

print("\nAngka rahasia adalah:", angka_rahasia)
print("Tebakanmu sebelumnya:", riwayat_tebakan)
print("Game selesai!")