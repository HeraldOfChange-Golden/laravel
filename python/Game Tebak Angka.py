import random

def game_tebak_angka():
    print("=== Game Tebak Angka ===")
    print("Saya telah memilih angka antara 1-100!")
    
    angka_rahasia = random.randint(1, 100)
    tebakan = 0
    percobaan = 0
    
    while tebakan != angka_rahasia:
        try:
            tebakan = int(input("Masukkan tebakan Anda: "))
            percobaan += 1
            
            if tebakan < angka_rahasia:
                print("Terlalu kecil! Coba lagi.")
            elif tebakan > angka_rahasia:
                print("Terlalu besar! Coba lagi.")
            else:
                print(f"Selamat! Anda berhasil menebak angka {angka_rahasia} dalam {percobaan} percobaan!")
                
        except ValueError:
            print("Masukkan angka yang valid!")

# Jalankan game
game_tebak_angka()