class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        res=0
        count = {}
        max_f = 0

        while r < len(s):

            # update count with new val
            count[s[r]] = 1 + count.get(s[r],0)

            max_f = max(max_f, count[s[r]])

            while (r-l+1) - max_f > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)
            r+=1
            
        return res
            