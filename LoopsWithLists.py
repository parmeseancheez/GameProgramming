print('💀')

names = ['jay','jamie','stu','xavier']

for item in names:
    print(item)

for num in range(0, len(names)):
    print(names[num])

for num in range(1,5):
    print(num)

for item in names:
    if (item == 'stu'):
        print('Stu is the best!')
    else:
        print(f'{item} is not so great')

# lets make an empty list first
perfectSquares = []
for num in range(1,11):
    square = num ** 2
    perfectSquares.append(square)

print(perfectSquares)

# this DOES NOT MAKE A COPY OF THE LIST
names2 = names
print(names)
print(names2)

names.append('julian')
print(names)
print(names2)

# THIS DOES MAKE A COPY OF THE LIST
names2 = names[:]