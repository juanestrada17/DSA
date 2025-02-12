# prices = [7,1,5,3,6,4]
prices = [7,5,1,5,10]

print(prices[1:])
# Objective = 
# Choose a day to buy stock and a future day to sell it
# Return max profit, else, 0 
def best_time_stock(prices):
    left, right = 0, 1 
    max_profit = 0 
    while right < len(prices):
        if prices[left] > prices[right]:
            left = right 
            right += 1
        else:
            current_savings = prices[right] - prices[left]
            max_profit = max(max_profit, current_savings)
            right += 1
    return max_profit
print(best_time_stock(prices))
        
         