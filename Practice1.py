myList = ['Jack', 'Sean', 'Mason', 'Charlie']

print(myList)

# append
myList.append('Ben')
print(myList)

# print sub
print(myList[2])

# insert
myList.insert(2,'Susan')
print(myList)

# append
myList.append('Gary')
print(myList)

# same things
for i in range(1,4):
    print(myList[i])
print(myList[1:4])

# complicated pop
myList.pop(myList.index('Susan'))
print(myList)

# insert
myList.insert(2, 'Susan')
print(myList)

# pop
someName = myList.pop()
print(someName)

# remove
myList.remove("Jack")
print(myList)

# printing myList indexes
print(myList[:3])
print(myList[2:])
print(myList[:])
