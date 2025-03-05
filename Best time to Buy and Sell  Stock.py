# Given an array prices[] of length N, representing the prices of the stocks on different days, the task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell.
#
# Note: Stock must be bought before being sold.
#
# Examples:
#
# Input: prices[] = {7, 10, 1, 3, 6, 9, 2}
# Output: 8
# Explanation: Buy for price 1 and sell for price 9.
prices= [7, 6, 4, 3, 1]
maxpr= 0
minpr =999999
for i in range(len(prices)):
    minpr = min(minpr , prices[i])
    maxpr = max(maxpr,prices[i] - minpr)
print(maxpr)