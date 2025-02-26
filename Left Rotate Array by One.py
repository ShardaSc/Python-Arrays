# Given an integer array nums, rotate the array to the left by one.

# Note: There is no need to return anything, just modify the given array.

# Examples:
# Input: nums = [1, 2, 3, 4, 5]

# Output: [2, 3, 4, 5, 1]

# Explanation: Initially, nums = [1, 2, 3, 4, 5]

# Rotating once to left -> nums = [2, 3, 4, 5, 1]

nums = [1, 2, 3, 4, 5]

count =nums[0]
nums.pop(0)
nums.append(count)
print(nums)

