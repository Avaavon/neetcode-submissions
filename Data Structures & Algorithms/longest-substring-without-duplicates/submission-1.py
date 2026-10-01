class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        cur_s = set()

        for r in range(len(s)):
            while s[r] in cur_s:
                cur_s.remove(s[l])
                l+=1
            cur_s.add(s[r])
            longest = max(longest,r-l +1)
        return longest

# time: O(n)
# space: O(n)