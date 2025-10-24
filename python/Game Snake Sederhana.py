import random
import time

def game_snake():
    print("=== Game Snake Sederhana ===")
    print("Kontrol: W (atas), A (kiri), S (bawah), D (kanan)")
    print("Tekan Q untuk keluar")
    
    # Inisialisasi papan 10x10
    papan = [[" " for _ in range(10)] for _ in range(10)]
    
    # Posisi awal snake
    snake = [(5, 5)]
    arah = "d"  # mulai ke kanan
    
    # Generate makanan pertama
    makanan = generate_makanan(snake, papan)
    
    score = 0
    
    while True:
        # Clear screen (sederhana)
        print("\n" * 50)
        
        # Update papan
        papan = [[" " for _ in range(10)] for _ in range(10)]
        
        # Gambar snake
        for x, y in snake:
            papan[y][x] = "●"
        
        # Gambar makanan
        papan[makanan[1]][makanan[0]] = "🍎"
        
        # Gambar border dan papan
        print("+" + "-" * 20 + "+")
        for baris in papan:
            print("|" + " ".join(baris) + " |")
        print("+" + "-" * 20 + "+")
        print(f"Score: {score}")
        print(f"Panjang snake: {len(snake)}")
        
        # Input arah
        arah_input = input("Arah (W/A/S/D/Q): ").lower()
        if arah_input == "q":
            print("Game dihentikan!")
            break
        elif arah_input in ["w", "a", "s", "d"]:
            arah = arah_input
        
        # Gerakkan snake
        kepala_x, kepala_y = snake[0]
        
        if arah == "w": kepala_y -= 1
        elif arah == "s": kepala_y += 1
        elif arah == "a": kepala_x -= 1
        elif arah == "d": kepala_x += 1
        
        # Cek tabrak border
        if kepala_x < 0 or kepala_x >= 10 or kepala_y < 0 or kepala_y >= 10:
            print("💥 GAME OVER! Tabrak border!")
            break
        
        # Cek tabrak diri sendiri
        if (kepala_x, kepala_y) in snake:
            print("💥 GAME OVER! Tabrak diri sendiri!")
            break
        
        # Gerakkan snake
        snake.insert(0, (kepala_x, kepala_y))
        
        # Cek makan makanan
        if (kepala_x, kepala_y) == makanan:
            score += 10
            makanan = generate_makanan(snake, papan)
        else:
            snake.pop()  # Hapus ekor jika tidak makan
        
        time.sleep(0.3)

def generate_makanan(snake, papan):
    while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if (x, y) not in snake:
            return (x, y)

# Jalankan game
game_snake()