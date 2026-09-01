class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq1 = {}
        for letter in s:
            freq1[letter] = 1 + freq1.get(letter,0)
        
        freq2 = {}
        for letter in t:
            freq2[letter] = 1 + freq2.get(letter,0)
        
        return freq1 == freq2