def game_kuis():
    print("=== Kuis Pengetahuan Umum ===")
    
    # List pertanyaan dan jawaban
    questions = [
        {
            "pertanyaan": "Apa ibukota Indonesia?",
            "jawaban": "jakarta"
        },
        {
            "pertanyaan": "Planet terdekat dengan matahari?",
            "jawaban": "merkuri"
        },
        {
            "pertanyaan": "2 + 2 x 2 = ?",
            "jawaban": "6"
        },
        {
            "pertanyaan": "Warna campuran merah dan biru?",
            "jawaban": "ungu"
        }
    ]
    
    score = 0
    
    for i, q in enumerate(questions, 1):
        print(f"\nPertanyaan {i}: {q['pertanyaan']}")
        jawaban_user = input("Jawaban: ").strip().lower()
        
        if jawaban_user == q['jawaban'].lower():
            print("✅ Benar!")
            score += 1
        else:
            print(f"❌ Salah! Jawaban yang benar: {q['jawaban']}")
    
    print(f"\n{'='*40}")
    print(f"Skor akhir: {score}/{len(questions)}")
    
    if score == len(questions):
        print("💫 LUAR BIASA! Semua jawaban benar!")
    elif score >= len(questions) // 2:
        print("👍 Bagus! Hasil yang memuaskan!")
    else:
        print("💪 Jangan menyerah, coba lagi!")

# Jalankan game
game_kuis()