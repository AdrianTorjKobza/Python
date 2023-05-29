class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        min = prices[0]
        prices_len = len(prices)

        for i in range(prices_len):
            if prices[i] < min:
                min = prices[i]
            elif (prices[i] - min) > profit:
                profit = prices[i] - min

        return profit

prices = [7, 1, 5, 3, 6, 4]
solution = Solution()

print(solution.maxProfit(prices)) # 5