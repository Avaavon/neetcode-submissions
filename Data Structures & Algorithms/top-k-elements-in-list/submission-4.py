class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create hashmap num:count
        # create buckets [[],[],[]] where index is freq
        # add elements to index of equivalent freq
        # start from end of freq
        # add elements k times

        count = {}

        for num in nums:
            count[num] = count.get(num,0) + 1
        
        freq = [[] for i in range(len(nums)+1)]

        for num, count in count.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

# time = O(n) + O(n) + O(n) = O(n)
# space = O(n)