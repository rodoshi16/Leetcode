class Solution:
    def maxArea(self, height: List[int]) -> int:
        #return max amount of water 
        l = 0 
        r = len(height) - 1 
        m = 0

        while l < r:
            a = (r-l) * min(height[l], height[r])
            m = max(m, a)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return m
        

