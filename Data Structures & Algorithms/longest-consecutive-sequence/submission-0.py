class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq=0
        myset=set(nums)
        for num in myset:
            length=0
            if num-1 not in myset:
                while num+length in myset:
                    length+=1
                longest_seq=max(longest_seq,length)
        return longest_seq