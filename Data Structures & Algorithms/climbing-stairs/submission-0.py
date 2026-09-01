"""
two variables
int one & int two

visualize steps from n total backwards

1) _ _ _ _ _ n

at the final step, ways to end = 1

2) _ _ _ _ _ 1

3) 8 5 3 2 1 1

NOTE: notice 1 -> 2 steps is different from 2 -> 1 steps
so starting from final stair case (1 value) 
reverse add 2 following steps

NOTE: if "one" and "two" are defined range is n-1
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        
        for i in range(n-1):
            tmp = one
            one = one + two
            two = tmp
        return one

"""
time = O(n)
space = O(1)
"""
