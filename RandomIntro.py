# to create random numbers, we must import the random module
# a module is code that someone else wrote that has useful functions

import random

someNumber = random.randint(1,100)
print(someNumber)


for num in range(1,10):
    someNumber = random.randint(1,100)
    print(someNumber)

# the random module also provides a way to randomly choose from a list
myList = ["coke","sprite","pepsi","7up","DrPepper"]
someItem = random.choice(myList)
print(someItem)

print(myList)
random.shuffle(myList)
print(myList)

while True:
    someNumber = random.randint(111111111,999999999)
    print(someNumber)
    input()