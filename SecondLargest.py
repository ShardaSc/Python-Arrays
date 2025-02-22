#Given an array of integers nums, return the second-largest element in the array.
# If the second-largest element does not exist, return -1.
# Input: nums = [8, 8, 7, 6, 5]
#
# Output: 7
#
# Explanation: The largest value in nums is 8, the second largest is 7

nums = [8, 8, 7, 6, 5]
for i in nums:
    re =list(set(nums))
    if len(re) < 2:
        print(-1)
    re.sort(reverse =True)
print(re[1])