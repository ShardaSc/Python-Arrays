# Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays.
# The elements in the union must be in ascending order.

# The union of two arrays is an array where all values are distinct and are present in either the first array,
# the second array, or both.

# Examples:
# Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]
#
# Output: [1, 2, 3, 4, 5, 7]
#
# Explanation: The elements 1, 2 are common to both, 3, 4, 5 are from nums1 and 7 is from nums2

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 7]

num3 = nums1 + nums2
num3 = sorted(set(num3))

print(num3)