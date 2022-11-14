seq =  [1,2,3,4]

for num in seq:
    print(num**2)

for num in seq:
    print('Hello')

salaries = {'John': 10, 'Sally': 20, 'Lisa': 30}

for employee in salaries:
    print(employee, end=' ')
    print('has a salary of ', end='')
    print(salaries[employee])

myPairs = [('a', 1), ('b', 2), ('b', 3)]

# tuple unpacking
for letter, num in myPairs:
    print(letter)
    print(num)

i = 1

while i < 5:
    print(f'i is currently {i}')
    i += 1

for x in range(0, 14, 2):
    print(x)

result = list(range(14))
print(result)

print('s' in 'kasjdflçajsldkfjlçaksjdflkajsdlkf')
print('z' in [1,2,3])