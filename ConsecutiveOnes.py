# Given a binary array nums, return the maximum number of consecutive 1s in the array.

# A binary array is an array that contains only 0s and 1s.

# Input: nums = [1, 1, 0, 0, 1, 1, 1, 0]
#
# Output: 3
#
# Explanation: The maximum consecutive 1s are present from index 4 to index 6, amounting to 3 1s

nums = [1, 0,1,1]

count = 0
max_count=0

for i in nums:
    if i == 1:
        count = count + 1
        max_count = max(max_count, count)
    else:
        count = 0
print(max_count)
