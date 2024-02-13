# while loops are used when you don't know how many times the loop should run

directions = "go"
while directions == "go":
    food = input("Name a food you like.")
    print(f"You like {food}")
    directions = input("Input 'go' to keep going or someting else to quit.")

print("\n\n")

# below we will use a boolean data type to check whether to keep going
active = True
while active:
    message = input("Indicate 'go' or 'stop'")
    if message == "go":
        print("You are now in a loop.")
    elif message == "stop":
        active = False
        print("You have left the loop.")
    else:
        message = input("PLEASE indicate 'go' or 'stop'")

print("\n\n")

while True:
    choice = input("'go' or 'stop' ")
    if choice == "go":
        print("You are going.")
    else:
        break
    print("You are still looping.")