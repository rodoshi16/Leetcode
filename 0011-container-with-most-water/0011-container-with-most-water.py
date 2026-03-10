class Solution:
    def maxArea(self, height: List[int]) -> int:

        l = 0 
        r = len(height) - 1
        m = 0 

        while l < r:
            a = min(height[l], height[r]) * (r-l)
            m = max(a, m)

            if height[l] < height[r]:
                l += 1 
            elif height[r] < height[l]:
                r-= 1 
            else:
                l += 1 
                r -= 1 
        
        return m 


