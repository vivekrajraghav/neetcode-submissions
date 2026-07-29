class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        max_profit=float("-inf")
        buy_price=float("inf")
        current_profit=float("-inf")
        for i in range(0,n):
            current_price=prices[i]
            buy_price=min(buy_price,current_price)
            current_profit=current_price-buy_price
            max_profit=max(max_profit,current_profit)
        return max_profit
