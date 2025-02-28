# Input: nums = [0, 2, 3, 1, 4]
#
# Output: 5
#
# Explanation: nums contains 0, 1, 2, 3, 4 thus leaving 5 as the only missing number in the range [0, 5]

nums = [0, 2, 3, 1, 4]
n = len(nums)
result = n * (n+1)//2
total= sum(nums)
print(result - total)