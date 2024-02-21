
# Double for loop
def maxProfit(prices):
    maxProfitNum = 0
    for numberOne in range(len(prices)):
        for numberTwo in prices[numberOne + 1:len(prices)]:
            if numberTwo - prices[numberOne] > maxProfitNum:
                maxProfitNum = numberTwo - prices[numberOne]
    return maxProfitNum


# Sliding window
def maxProfit2(prices):
    l = 0
    mProfit = 0

    for index in range(1, len(prices)):
        if prices[index] > prices[l]:
            profit = prices[index] - prices[l]
            mProfit = max(profit, mProfit)
        else:
            l = index
    return mProfit


print(maxProfit2([3, 3, 5, 0, 0, 4]))
