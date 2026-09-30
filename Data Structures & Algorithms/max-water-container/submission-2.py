class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_area = 0

        i = 0
        j = len(heights) - 1

        while i<j:
            min_height = min(heights[i],heights[j])
            temp_area = min_height * (j-i)
            max_area = max(max_area,temp_area)
            if heights[i]>heights[j]:
                j-=1
            elif heights[j]>heights[i]:
                i+=1
            else:
                i+=1
        return max_area

# time: O(n)
# space: O(1)