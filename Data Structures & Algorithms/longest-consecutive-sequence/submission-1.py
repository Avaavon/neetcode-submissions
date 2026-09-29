class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_set = set(nums)
        longest = 0

        for num in new_set:
            if num-1 not in new_set:
                count = 1
                while num+1 in new_set:
                    count+=1
                    num+=1
                longest = max(longest,count)
        return longest

# time: O(n)
# space: O(n)