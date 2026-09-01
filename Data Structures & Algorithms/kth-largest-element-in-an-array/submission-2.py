"""
solution 2: use min-heap

time: nlogk
space: k

"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]