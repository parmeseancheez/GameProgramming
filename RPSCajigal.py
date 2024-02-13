#Sean Cajigal

import random

choices = ["rock","paper","scissors"]

wins = 0
losses = 0

while True:
    playerInput = input("\nRock, paper, or scissors? ")
    playerInput = choices.index(playerInput)

    computerInput = random.randint(0,2)

    print(f"\nComputer: {choices[computerInput]} | Player: {choices[playerInput]}")
    if playerInput > computerInput or (playerInput == 0 and computerInput == 2):
        print("\nPlayer wins! Yippie!")
        wins+=1
    elif playerInput < computerInput or (playerInput == 2 and computerInput == 0):
        print("\ncomputer wins uh oh")
        losses+=1
    else:
        print("\ntie")

    print(f"\nWins: {wins} | Losses: {losses}")

    if input("\nWant to play again? Enter 'quit' to stop; anything else to play again. ") == "quit": break

