# Write
# a
# Python
# function
# that
# takes
# a
# string as input and returns
# the
# length
# of
# the
# longest
# substring
# without
# repeating
# characters.

def reversefun(s):
    char_list = list(s)
    char_list.reverse()
    return ''.join(char_list)
def reverse_with_slicing(s):
    return s[::-1]

def reverse_with_loop(s):
    s1 = ""
    for i in reversed(s):
        s1 += i
    return s1

s = "longestsubstring"
print(reverse_with_slicing(s))
print(reverse_with_loop(s))
print(reversefun(s))


