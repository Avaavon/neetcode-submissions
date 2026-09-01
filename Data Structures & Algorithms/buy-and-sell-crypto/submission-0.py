class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1
        max_v=0

        while right<len(prices):
            profit = prices[right]-prices[left]

            if prices[left]<=prices[right]:
                max_v = max(max_v,profit)
                right+=1
            else:
                left=right
                right+=1
        return max_v

