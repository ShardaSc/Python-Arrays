# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

nums = [2,7,11,15]

target = 9
count = 0
result = []
for index,value in enumerate(nums):
    count = count + value
    result.append(value)

    if count == target:
        for index in range(len(result)):
            print(index)

