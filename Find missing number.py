# Given an integer array of size n containing distinct values in the range from 0 to n (inclusive), return the only number missing from the array within this range.
#
#
# Examples:
# Input: nums = [0, 2, 3, 1, 4]
#
# Output: 5
#
# Explanation: nums contains 0, 1, 2, 3, 4 thus leaving 5 as the only missing number in the range [0, 5]

nums = [0, 2, 3, 1, 4]

n = len(nums)
anums = n * (n+1) // 2
result = sum(nums)
print(anums-result)