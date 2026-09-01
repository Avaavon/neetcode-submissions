"""
solution 1: use min-heap

time:
space: 

"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]