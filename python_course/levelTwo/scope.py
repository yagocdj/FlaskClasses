# LEGB RULE LOCAL -> ENCLOSING -> GLOBAL -> BUILT IN (LOCAL IS THE FIRST)

# EXAMPLE 1

# def report():
#     # LOCAL ASSIGNMENT!
#     x = 'local'
#     print(x)

# EXAMPLE 2

# x = 'THIS IS GLOBAL LEVEL'

# def enclosing():
#     # Python will find this x variable to be printed by inside() (ENCLOSING)
#     x = 'Enclosing level'

#     def inside():
#         # LEGB
#         # There is no x in this scope. Thus, python'll search for it in the enclosing()
#         print(x)
    
#     inside()

# enclosing()

# EXAMPLE 3

# x = 'THIS IS GLOBAL LEVEL'

# def enclosing():
#     # x = 'Enclosing level'

#     def inside():
#         # LEGB
#         # There is no x in this scope. Thus, python'll search for it in the enclosing()
#         print(x)
    
#     inside()

# enclosing()

# SUMMARY

# if python doesn't find the built-in x, an error will be raised
# x = 'GLOBAL X'

# def enclosing():
#     x = 'ENCLOSING X'

#     def inside():
#         x = 'LOCAL X'
#         print(x)
    
#     inside()

# enclosing()

# global statement

x = 'outside'

def report():
    # HEY GRAB THE GLOBAL LEVEL x VARIABLE
    global x
    # REASSING GLOBAL x
    x = 'inside'
    return x

print(report())
print(x)
