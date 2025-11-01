class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mins = [prices[0]]
        for i in range(1, len(prices)):
            if mins[-1] > prices[i]:
                mins.append(prices[i])
            else:
                mins.append(mins[-1])
            # print(mins)
        
        answer = 0
        for i in range(len(prices) - 1):
            answer = max(answer, prices[i + 1] - mins[i])

        return answer