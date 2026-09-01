"""
time to reach target = (target - position) / speed

step 1: sort the positions, speed pairs where position top/end is smallest
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs =  sorted(zip(position, speed), reverse = True)

        for p, s in pairs:
            arrival_time = (target - p) / s
            stack.append(arrival_time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

