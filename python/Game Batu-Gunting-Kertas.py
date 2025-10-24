import random

def game_batu_gunting_kertas():
    print("=== Game Batu-Gunting-Kertas ===")
    print("Pilihan:")
    print("1. Batu")
    print("2. Gunting")
    print("3. Kertas")
    
    pilihan = ["Batu", "Gunting", "Kertas"]
    
    while True:
        try:
            user_choice = int(input("Masukkan pilihan (1-3) atau 0 untuk keluar: "))
            
            if user_choice == 0:
                print("Terima kasih telah bermain!")
                break
            elif user_choice < 1 or user_choice > 3:
                print("Pilihan tidak valid!")
                continue
            
            user_choice -= 1  # Konversi ke index 0-based
            computer_choice = random.randint(0, 2)
            
            print(f"\nAnda memilih: {pilihan[user_choice]}")
            print(f"Computer memilih: {pilihan[computer_choice]}")
            
            # Logika permainan
            if user_choice == computer_choice:
                print("Hasil: SERI!")
            elif (user_choice == 0 and computer_choice == 1) or \
                 (user_choice == 1 and computer_choice == 2) or \
                 (user_choice == 2 and computer_choice == 0):
                print("Hasil: ANDA MENANG!")
            else:
                print("Hasil: ANDA KALAH!")
                
            print("-" * 30)
            
        except ValueError:
            print("Masukkan angka yang valid!")

# Jalankan game
game_batu_gunting_kertas()