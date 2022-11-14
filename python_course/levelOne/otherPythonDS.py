# TUPLES 
t = (1, 2 ,3, 'a', 2.3)
# t[0] = 'NEW' -> the interpreter will raise an error
print(t)
print(t[0])

# SETS

x = set()
print(x)
x.add(1)
x.add(2)
x.add(3)
# the following numbers won't be added to the set, since the set data structure allows only one copy of that element in it
# x.add(3)
# x.add(3)
print(x)
randomList = [1, 2, 12, 3, 2, 2, 2, 21, 1, 1, 1, 1, 2, 3, 4, 4]
print(set(randomList))

# BOOLEANS

a = True
b = False
# SPECIAL KEYWORD
c = None
print(a)
print(1 > 2)
print(1 < 2)