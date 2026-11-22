class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sort first so we can stop earlier
        nums.sort()
        res = []

        # recursive function that
        # inputs: i, currentList, total
        # 1) calculates total
        # 2) if total == target: add to res
        # 3) if total > target end loop

        def dfs(i,currentList,total):
            if total == target:
                    res.append(currentList.copy())
                    return

            for j in range(i,len(nums)):
                if total + nums[j] > target:
                    return

                currentList.append(nums[j])
                dfs(j,currentList,total + nums[j])
                currentList.pop()

        dfs(0,[],0)
        return res

        # time: O(2 t/m)
        # space: O(t/m)
        # where t = target & m = min val in nums


            
