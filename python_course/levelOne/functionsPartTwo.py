# max and min

print(max(10, 3))
print(max([1, 4, 7, 12, 100]))

print(min(1, 100))
print(min([1, 4, 7, 12, 100]))

# enumerate
myList = ['a', 'b', 'c']

for index, item in enumerate(myList):
    print('\n'+item)
    print(f'is at index {index}')

# .join
myList.append('d')
myListTwo = myList

# '' is the conector
print('\n' + '--'.join(myList))

# PROBLEM 1
def has_secret_word(string: str) -> bool:
    return 'secret' in string.lower()

print('\n', has_secret_word('this is a Secret'))

# PROBLEM 2
def encode_x(string: str) -> str:
    for letter in string:
        string = string.replace(letter, 'x') if letter.lower() in 'aeiou' else string
    return string

# TODO - try making this function using recursion

testString = "Adam"
print(encode_x(testString))
