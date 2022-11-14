myList = ['a', 'b', 'c', 'd', 'e']
print(myList[1:4])
myList.append('z')
myList.insert(0, 'z')
poppedItem = myList.pop(0)  # default -> pops an item from the last position

print(myList)
print(poppedItem)

myListOne = [0, 1, 2]
myListTwo = [3, 4, 5]
myListThree = [6, 7, 8]

megaList = [myListOne, myListTwo, myListThree]
print(megaList)
print(len(megaList))
print(megaList[0])
print(megaList[0][1])