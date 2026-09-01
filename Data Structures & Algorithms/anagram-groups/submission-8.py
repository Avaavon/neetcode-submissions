class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        orderedHash={}

        for word in strs:
            orderedWord=''.join(sorted(word))

            if orderedWord in orderedHash:
                orderedHash[orderedWord]+=[word]
            else:
                orderedHash[orderedWord]=[word];
        return list(orderedHash.values())