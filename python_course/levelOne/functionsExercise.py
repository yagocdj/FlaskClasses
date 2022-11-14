# Function Tasks
#
#
# Let's see if you can solve these word problems by creating functions.
# The function "skeleton" has been set up for you to fill in below the problem
# description, as well as example outputs of what the function should return
# given certain inputs. Best of luck, some of these will be challenging!
#
# The tasks will start off easy and proceed to get harder and harder.

# ## Task 1
#
#  Create a function that takes in two integers and returns
## a Boolean True if their sum is 10, False if their sum is something else.


def check_ten(n1,n2):
    return (n1 + n2) == 10


# print(check_ten(3,4))  # False
# print(check_ten(7,3))  # True
# print(check_ten(9,0))  # False


# ## Task 2
#
# Create a function that takes in two integers and returns True if their
# sum is 10, otherwise, return the actual sum value.


def check_ten_sum(n1,n2):
    return True if (n1 + n2) == 10 else n1 + n2


# print(check_ten_sum(1,4))  # 5
# print(check_ten_sum(9,1))  # True
# print(check_ten_sum(10,10))  # 20
# print(check_ten_sum(6,4))  # True

# ## Task 3
#
# Create a function that takes in a string and returns back the
# first character of that string in upper case.



def first_upper(mystring):
    return mystring[0].upper()

# testString = 'pizza de alface'
# print(first_upper(testString))  # P


# ## Task 4
#
# Create a function that takes in a string and returns the last two characters.
# If there are less than two chracters, return the string:  "Error".
# Use this link if you need help/hint.
# (https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string)



def last_two(mystring):
    try:
        assert len(mystring) >= 2
        return mystring[-2:]
    except AssertionError:
        return 'Error'


# print(last_two('Zap'))
# print(last_two('a'))
# print(last_two('IFPB'))
# print(last_two(''))
# print(last_two('Eu me chamo Yago'))


# ## Task 5
#
# Given a list of integers, return True if the sequence [1,2,3] is somewhere
# in the list. Hint: Use slicing and a for loop.


def seq_check(nums):
    for i in range(len(nums) - 2):
        if nums[i:i+3] == [1,2,3]:
            return True
    return False

# print(seq_check([1,1,1,2,3]))
# print(seq_check([1,1,1,2,2,3]))
# print(seq_check([1,2,3]))


# ## Task 6
#
# Given a 2 strings, create a function that returns the difference in length
# between them. This difference in length should always be a positive number
# (or just 0). Hint: Absolute Value.**



def compare_len(s1: str,s2: str) -> int:
    """
    # solution 1
    len_diff = len(s1) - len(s2)
    return -(len_diff) if len_diff < 0 else len_diff
    """
    # solution 2
    return abs(len(s1) - len(s2))

# print(compare_len('água', 'farinha'))
# print(compare_len('vitória', 'treze'))
# print(compare_len('um', 'trinta e nove'))
# print(compare_len('setecentos e quarenta e cinco', 'casa'))


# ## Task 7
#
# Given a list of integers, if the length of the list is an even number,
# return the sum of the list. If the length of the list is odd, return the max
## value in that list.



def sum_or_max(mylist):
    return sum(mylist) if len(mylist) % 2 == 0 else max(mylist)

# print(sum_or_max([9, 7, 5, 2, 4, 13, 3]))
# print(sum_or_max([1, 1, 1, 1, 1, 1]))
