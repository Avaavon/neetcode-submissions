# go thru list put each val into stack but check if greater than cur tops
# pop the old tops until the new top is less than prev
# for each pop compare th

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        # monotonic decreasing (top largest)
        # pair: [temp, index]
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append((t,i))
        return res
            

