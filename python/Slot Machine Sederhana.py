import random

def game_slot():
    print("=== Game Slot Machine ===")
    print("Simbol: 🍒 🍋 🍊 🍇 🔔 ⭐")
    
    koin = 100
    
    simbol = ["🍒", "🍋", "🍊", "🍇", "🔔", "⭐"]
    
    while koin > 0:
        print(f"\nKoin Anda: {koin}")
        print("1. Putar (10 koin)")
        print("2. Keluar")
        
        pilihan = input("Pilih: ")
        
        if pilihan == "2":
            print(f"Anda keluar dengan {koin} koin!")
            break
        elif pilihan == "1":
            if koin < 10:
                print("Koin tidak cukup!")
                continue
            
            koin -= 10
            
            # Putar slot
            print("\nMemutar...")
            hasil = [random.choice(simbol) for _ in range(3)]
            
            print("+" + "-" * 13 + "+")
            print(f"| {hasil[0]} | {hasil[1]} | {hasil[2]} |")
            print("+" + "-" * 13 + "+")
            
            # Cek kemenangan
            if hasil[0] == hasil[1] == hasil[2]:
                if hasil[0] == "⭐":
                    menang = 100
                    print("🎊 JACKPOT! +100 koin!")
                else:
                    menang = 50
                    print("🎉 TIGA SEJENIS! +50 koin!")
            elif hasil[0] == hasil[1] or hasil[1] == hasil[2]:
                menang = 20
                print("👍 DUA SEJENIS! +20 koin!")
            else:
                menang = 0
                print("😞 Coba lagi!")
            
            koin += menang
        
        else:
            print("Pilihan tidak valid!")
    
    if koin <= 0:
        print("\n💸 Koin habis! Game over!")

# Jalankan game
game_slot()