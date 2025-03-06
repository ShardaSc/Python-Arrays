#Given an array you have to create list of each item

# Input = [1,2,3,4,5,6]
#
# Output =[[1],[2],[3],[4],[5],[6]]

arr = [1,2,3,4,5,6]

result = [[item] for item in arr]

print(result)