'''
We developed several algorithms for this problem in the introduction. Specifically, on
Page2we showed how to compute the maximum profitby computing the difference of the current
entry with the minimum value seen so far as we iterate through the array.
For example, the array of minimum values seen so far for the given example is
<310,370,275,275,2@,260,260,230,230,230>. The maximum profit that can be made by selling
on each specific day is the difference of the current price and the minimum seen so far, i.e.,
<0,5,0,20,0,10,30,0,25,20). The maximum profit overall is 30, corresponding to buying 260 and
selling for 290.

walk through
given arr = [7,1,5,3,6,4]
minimum seen soo far will be - [7,1,1,1,1,1]
take the differece -> arr - minimum_so_far
        res =  [0,0,4,2,5,3]

    The time complexity is O(n) and the space complexity is O(1), where n is the length of the array
'''


class Solution:
    def maxProfit(self, prices):
        minimum_price_so_far, max_profit = float('inf'), 0
        for price in prices:
            max_profit_sell_today = price - minimum_price_so_far
            max_profit = max(max_profit, max_profit_sell_today)
            minimum_price_so_far = min(minimum_price_so_far, price)
        return max_profit

prices = [7,1,5,3,6,4]
o1 = Solution()
print(o1.maxProfit(prices))

prices = [7,6,4,3,1]
print(o1.maxProfit(prices))