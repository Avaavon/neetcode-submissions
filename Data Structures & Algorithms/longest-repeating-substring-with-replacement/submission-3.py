class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left=0 #left index
        char_count={} #dict of char:count
        max_f=0 #max freq char count
        res=0

        for right in range(len(s)):#right index
            char_count[s[right]]= 1 + char_count.get(s[right],0) #add to curr char count in dict
            max_f= max(max_f,char_count[s[right]]) #compare new char size to max char size
            while (right-left+1)-max_f > k:
                char_count[s[left]]-=1
                left+=1
            res=max(res,right-left+1)
        return res




            
            
            

            