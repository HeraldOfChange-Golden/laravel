import random

def game_hangman():
    print("=== Game Hangman ===")
    
    kata_list = ["python", "programming", "computer", "algorithm", "developer", "software"]
    kata_rahasia = random.choice(kata_list)
    tebakan = ["_"] * len(kata_rahasia)
    kesempatan = 6
    huruf_tebakan = []
    
    print("Kata yang harus ditebak:", " ".join(tebakan))
    print(f"Kesempatan salah: {kesempatan}")
    
    while kesempatan > 0 and "_" in tebakan:
        huruf = input("\nTebak satu huruf: ").lower()
        
        if len(huruf) != 1 or not huruf.isalpha():
            print("Masukkan satu huruf saja!")
            continue
            
        if huruf in huruf_tebakan:
            print("Anda sudah menebak huruf ini!")
            continue
            
        huruf_tebakan.append(huruf)
        
        if huruf in kata_rahasia:
            print(f"✅ Huruf '{huruf}' benar!")
            for i in range(len(kata_rahasia)):
                if kata_rahasia[i] == huruf:
                    tebakan[i] = huruf
        else:
            kesempatan -= 1
            print(f"❌ Huruf '{huruf}' salah! Kesempatan tersisa: {kesempatan}")
        
        print("\nKata:", " ".join(tebakan))
        print(f"Huruf yang sudah ditebak: {', '.join(huruf_tebakan)}")
    
    # Cek hasil
    if "_" not in tebakan:
        print(f"\n🎉 SELAMAT! Anda menebak kata: {kata_rahasia}")
    else:
        print(f"\n💀 GAME OVER! Kata yang benar: {kata_rahasia}")

# Jalankan game
game_hangman()