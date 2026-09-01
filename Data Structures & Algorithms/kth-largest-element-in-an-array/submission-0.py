"""
solution 1: use sort

time = nlogn bc timsort
note* timsort is split by runs -> insertion sort -> merge sort
space = O(1)
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]