import random

wins = 0
losses = 0

# Game Loop
playing = True
while playing:
    # Initialize game!
    number = random.randint(1,100)
    tries = 6
    #print(number)

    # Fancy Text
    print("\nNEW GAME START\n")
    while tries > 0:
        # Ask the player for input (Their guessed number)
        guess = int(input("Guess a number between 1 and 100: "))

        # Check number
        if guess > number:
            print("Too high!!!\n")
        elif guess < number:
            print("Too low!!!\n")
        elif guess == number:
            print("Yippie! You won!\n")
            break
        else:
            print("What?\n")

        # Use up a try
        tries -= 1

    # After game, celebrate if player won!
    if tries == 0:
        losses += 1
        print(f"Better luck next time! [ {wins} Wins / {losses} Losses ]")
    else:
        wins += 1
        print(f"Good job! [ {wins} Wins / {losses} Losses ]")

    # Ask the player for input (If they want to play again)
    if input("'Enter key' to play again. 'quit' to stop playing. ") == "quit":
        playing = False