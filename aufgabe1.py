import random

def rps(p1, p2):
    """Bestimmt den Gewinner von Rock, Paper, Scissors."""
    p1 = p1.lower()
    p2 = p2.lower()

    if p1 == p2:
        return "Draw!"

    winning_pairs = {
        ("rock", "scissors"),
        ("scissors", "paper"),
        ("paper", "rock")
    }

    if (p1, p2) in winning_pairs:
        return "Player 1 won!"
    else:
        return "Player 2 won!"


# --- Spielschleife mit Bot-Gegner ---
while True:
    print("\nRock, Paper, Scissors!")
    print("Mögliche Eingaben: rock, paper, scissors")

    # Spielerzug
    player_move = input("Dein Zug: ").strip().lower()

    # Eingabe prüfen
    if player_move not in ["rock", "paper", "scissors"]:
        print("Ungültige Eingabe, bitte rock/paper/scissors schreiben.")
        continue

    # Bot-Zug (zufällig)
    bot_move = random.choice(["rock", "paper", "scissors"])
    print("Bot spielt:", bot_move)

    # Ergebnis bestimmen
    ergebnis = rps(player_move, bot_move)

    if ergebnis == "Draw!":
        print("Unentschieden!")
    elif ergebnis == "Player 1 won!":
        print("Du hast gewonnen! 🎉")
    else:
        print("Der Bot hat gewonnen 😈")

    # nochmal?
    nochmal = input("Nochmal spielen? (j/n): ").strip().lower()
    if nochmal != "j":
        print("Tschüss!")
        break

