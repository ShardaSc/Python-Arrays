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


#Using Slicing window
def longest_unique_substring_length(s):
    char_index = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len

#Using Set and Two Pointers
def longest_unique_substring_set(s):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len

s = "abcabcbb"
print(longest_unique_substring_length(s))
print(longest_unique_substring_set(s))