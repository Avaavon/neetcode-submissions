class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) # 0-26 hash to value of count
        for s in strs:
            count = [0] * 26
            for letter in s:
                count[ord(letter) - ord('a')] += 1
            anagrams[tuple(count)].append(s)
        
        return list(anagrams.values())

#time: O(n*m) where n is size of strs and m is size of a string
#space: O(n*m)
