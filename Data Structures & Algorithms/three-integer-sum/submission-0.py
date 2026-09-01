class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        
        for i,element in enumerate(nums):
            

            #if the first element(smallest of 3)
            #is greater than 0, break
            if element>0:
                break
            
            #if the index is greater than 0 
            #and the element is the same as previous, continue
            if i>0 and element == nums[i-1]:
                continue

            left=i+1
            right=len(nums)-1

            while left<right:
                curr_sum = element + nums[left] + nums[right]

                if curr_sum<0:
                    left+=1
                elif curr_sum>0:
                    right-=1
                else:
                    res.append([element, nums[left], nums[right]])
                    left+=1
                    right-=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
        return res

                
                