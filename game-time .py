
import random

CHOICES = {
    "tosh": "q",
    "qaychi": "s",
    "qog'oz": "p"
}

SHORT_TO_NAME = {v: k for k, v in CHOICES.items()}

def get_computer_choice():
    return random.choice(list(SHORT_TO_NAME.keys()))

def get_player_choice():
    prompt = ("Tanlang (tosh, qaychi, qog'oz) yoki qisqa: (q for tosh, s for qaychi, p for qog'oz)\n"
              "Chiqish uchun 'chiq' yoki 'exit' kiriting: ")
    while True:
        raw = input(prompt).strip().lower()
        if raw in ("chiq", "exit"):
            return None

        if raw in CHOICES:
            return CHOICES[raw]
        if raw in SHORT_TO_NAME:
            return raw
        print("Noto'g'ri tanlov. Iltimos: tosh, qaychi yoki qog'oz (yoki q/s/p).")

def decide_winner(player, comp):

    if player == comp:
        return "teng"

    wins = {
        'q': 's',  # tosh qaychini yutadi
        's': 'p',  # qaychi qog'ozni yutadi
        'p': 'q'   # qog'oz toshni yutadi
    }
    if wins[player] == comp:
        return "player"
    else:
        return "computer"

def play_round():
    player = get_player_choice()
    if player is None:
        return None  
    comp = get_computer_choice()
    result = decide_winner(player, comp)

    print(f"Siz: {SHORT_TO_NAME[player]}  —  Kompyuter: {SHORT_TO_NAME[comp]}")
    if result == "teng":
        print("Natija: Durang!")
    elif result == "player":
        print("Natija: Siz yutdingiz! 🎉")
    else:
        print("Natija: Kompyuter yutdi. 😅")
    return result

def main():
    print("=== Tosh - Qaychi - Qog'oz o'yini ===")

    while True:
        try:
            best_of = int(input("Eng yaxshi nechta raund (masalan, 3 uchun 3) yoki 0 — cheksiz: ").strip())
            if best_of < 0:
                print("Manfiy raqam bo'lishi mumkin emas.")
                continue
            break
        except ValueError:
            print("Iltimos butun son kiriting.")
    needed = None
    if best_of > 0:

        needed = best_of // 2 + 1

    player_score = 0
    comp_score = 0
    rounds_played = 0

    while True:
        print("\n--- Yangi raund ---")
        res = play_round()
        if res is None:
            print("O'yindan chiqildi. Rahmat!")
            break
        rounds_played += 1
        if res == "player":
            player_score += 1
        elif res == "computer":
            comp_score += 1

        print(f"Hisob: Siz {player_score} — Kompyuter {comp_score}  (Raundlar: {rounds_played})")

        if needed is not None:
            if player_score >= needed:
                print(f"\nSiz umumiy g'olib bo'ldingiz! Yakuniy hisob: {player_score} — {comp_score}")
                break
            if comp_score >= needed:
                print(f"\nKompyuter umumiy g'olib bo'ldi. Yakuniy hisob: {player_score} — {comp_score}")
                break


        if needed is None:
            again = input("Yana o'ynaysizmi? (ha/yo'q): ").strip().lower()
            if again not in ("ha", "h", "yes", "y"):
                print("O'yin tugadi. Rahmat!")
                break

if __name__ == "__main__":
    main()
