# def hello(name='Jose'):
#     print('The hello() func has been run')

#     def greet():
#         return "    This is inside the greet()"

#     def welcome():
#         return "    This is inside welcome()"
    
#     return greet if name == 'Jose' else welcome


# # x = greet
# x = hello(name="Sammy")

# print(x())

# def hello():
#     return "Hi Jose!"

# def other(func):
#     print("Some other code")
#     # Assume that func passed in is a function!!!
#     print(func())

# other(hello)

def new_decorator(func):
    
    def wrap_func():
        print("some code before executing func")

        func()

        print('Code here, after executing func()')

    return wrap_func

@new_decorator
def func_needs_decorator():
    print('Please decorate me')

# func_needs_decorator = new_decorator(func_needs_decorator)  # this is the same as using @new_decorator
func_needs_decorator()
