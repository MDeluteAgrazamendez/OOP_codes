from Playing_Cards import *

def main():
    deck = Playing_Card_Deck()
    deck.shuffle()

    player1_score = 0
    player2_score = 0

    print("====================================")
    print("      HIGH CARD GAME (5 ROUNDS)")
    print("====================================")

    for round in range(1, 6):
        print(f"\n========== ROUND {round} ==========")

        # Deal one card to each player
        player1 = deck.deal()
        player2 = deck.deal()

        # Display each player's hand
        print("Player 1's Hand:", player1)
        print("Player 2's Hand:", player2)

        # Determine the round winner
        if player1 > player2:
            print("\nWinner of Round", round, ": Player 1")
            player1_score += 1
        elif player2 > player1:
            print("\nWinner of Round", round, ": Player 2")
            player2_score += 1
        else:
            print("\nWinner of Round", round, ": Tie")

        # Display current score
        print(f"\nCurrent Score")
        print(f"Player 1: {player1_score}")
        print(f"Player 2: {player2_score}")

    # Display final results
    print("\n====================================")
    print("          FINAL RESULTS")
    print("====================================")

    print(f"Player 1 Final Score: {player1_score}")
    print(f"Player 2 Final Score: {player2_score}")

    if player1_score > player2_score:
        print("\n🏆 OVERALL WINNER: PLAYER 1")
    elif player2_score > player1_score:
        print("\n🏆 OVERALL WINNER: PLAYER 2")
    else:
        print("\n🤝 THE GAME ENDED IN A TIE")

if __name__ == "__main__":
    main()