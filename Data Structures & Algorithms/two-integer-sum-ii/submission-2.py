class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1

        while start<end:
            total = numbers[start]+numbers[end]

            if total> target:
                end-=1
                continue
            if total<target:
                start+=1
                continue
            else:
                return [start+1,end+1]
            
# space: O(1) pointers
# time: O(n)