# Given an array find the targeted element and if the element is not in arr return -1
# Input: nums = [2, 3, 4, 5, 3], target = 3
#
# Output: 1
#
# Explanation: The first occurence of 3 in nums is at index 1

#Traverse the arr and check for each element
def linearsearch(nums,target):
    for i in range(len(nums)):
        if nums[i] == target:
            print(i)
            return
    print(-1)

nums = [2, 3, 4, 5, 3]
target = 4
linearsearch(nums,target)
