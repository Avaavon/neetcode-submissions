class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        cur_map = {} # char : freq
        res = 0

        l = 0

        for r in range(len(s)):
            cur_map[s[r]] = cur_map.get(s[r],0) + 1
            maxf = max(maxf, cur_map[s[r]])

            while ((r-l+1) - maxf) > k:
                cur_map[s[l]] -=1
                l+=1
            res = max(res, r-l+1)

        return res

# create a sliding window
# check r-l+1 - maxfrequency of some char is < k
# time: O(n)
# space: O(n) where n is unique chars