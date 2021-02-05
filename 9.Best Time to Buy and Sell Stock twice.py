'''
 Consider it as state machine state machine, A, B, C, D

rest    holding  resting  holding
 0 ------> A ------> B ------> C ----> D
 |    buy  |  sell      buy       sell |
 |         |                           |
 |         |                           |
 ^         |---------------------------| ----> We need to consider these 4 states
 we dont have any money intially so consider it as 0th state

 So there are 2 things here to consider
 1. Buying                             2. Selling
 max(STATE, X - price)                     max(STATE, X + price)
 where X is a previous state
 now I need to convert this state Machine to Code

'''

class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        # start making state machine, A, B, C, D
        A = -prices[0]  # Will assign to the first element in the prices, -ve
        # sign bcoz as we are buyinh at A state, our profit will be -ve or decreasing
        B = float('-inf')  # remaining state I will assign -ve inf as there values will change
        C = float('-inf')
        D = float('-inf')

        for price in prices:
            A = max(A, -price)  # in state A we have 2 options ie either we can stay in A or we can buy the stock ie -price
            B = max(B, A + price)  # we can stay in B(we are waiting to sell the stock)
            # or we can buy the stock from A and sell it at what ever the price
            # we have at B, as we are changing the states here from A to B we do A+price, +price bcoz we are selling it
            C = max(C, B - price)  # we can hold in C ie the current state or
            # we can buy it, as we are changing states here B - price
            D = max(D, C + price)  # finally we have D, which will be our last state
            # we can just hold it D(selling) or C+price as we are selling

        return D

prices = [3,3,5,0,0,3,1,4]
o1 = Solution()
print(o1.maxProfit(prices))

prices = [1,2,3,4,5]
print(o1.maxProfit(prices))