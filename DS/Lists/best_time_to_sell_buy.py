"""
Write a program that takes an array denoting the daily stock price,
 and retums the maximum profit that could be made by buying and
  then selling one share of that stock.
 There is no need to buy if no profit is possible.
"""

def maxProfit(prices):
        max_profit=float("-inf")
        prev=prices[0]

        for i in range(1, len(prices)):
            profit_to_sell_today = prices[i] - prev
            max_profit=max(max_profit , profit_to_sell_today)
            prev = min(prev , prices[i])
        return max_profit if max_profit > 0 else 0

if __name__ == "__main__":
    print(maxProfit([310,315,275,295,260,270,290,230,255,250]))
    # 30
