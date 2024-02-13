favNum = int(input("What is your favorite number, (1-100)"))
print(favNum)
if favNum > 75:
    print("That's a large number.")
elif (favNum > 30 and favNum <= 75):
    print("That's a medium number.")
else:
    print("That's NOT a large number.")

if favNum % 2 == 0:
    print("You like even numbers.")
else:
    print("You like odd numbers.")

if favNum % 5 == 0:
    print("This number is a multiple of five.")
else:
    print("This number is not a multiple of five.")