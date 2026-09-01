"""
backtracking
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp = []

        def backtrack(index):
            # base case
            if index == len(nums):
                res.append(tmp[:])
                return
            
            # option 1: no add
            backtrack(index+1)

            # option 2: add
            tmp.append(nums[index])
            backtrack(index+1)
            tmp.pop()
        
        backtrack(0)
        return res

