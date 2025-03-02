# Given an integer array nums and a non-negative integer k, rotate the array to the left by k steps.
#
#
# Examples:
# Input: nums = [1, 2, 3, 4, 5, 6], k = 2
#
# Output: nums = [3, 4, 5, 6, 1, 2]
#
# Explanation: rotate 1 step to the left: [2, 3, 4, 5, 6, 1]
#
# rotate 2 steps to the left: [3, 4, 5, 6, 1, 2]

nums = [1, 2, 3, 4, 5, 6]
k = 2
n =len(nums)
k =k % n
nums[:] = nums[k:] +nums[:k]
print(nums)