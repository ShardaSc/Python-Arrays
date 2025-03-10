# You are given an array of integers. Write a function that returns a new array where each element is squared,
# but only if it is an even number. Use the map() function to achieve this.

# Input: [1, 2, 3, 4, 5, 6]
# Output: [1, 4, 3, 16, 5, 36]

nums = [1, 2, 3, 4, 5, 6]

result = list(map(lambda x:x * x if x%2 == 0 else x,nums))

print(result)
