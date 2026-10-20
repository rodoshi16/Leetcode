class Solution:
    def trap(self, height: List[int]) -> int:
        #input: list of height values
        # out: how much water it can trap after raining 

        # want to maximize the amount of water
        # always capped by the lowest wall, ex: right is 9, left is 1 - spills all the water
        # we need max of left wall and max of right wall
        # water trapped is always min(l, r)
        # if leftmax < rightmax -> move right
        # if rightmax < leftmax -> move left


        n = len(height)
        l, leftMax = 0, height[0]
        r, rightMax = n - 1, height[n -1]
        res = 0 

        while l < r:
            if leftMax < rightMax:
                l += 1 
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]


            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
            
        return res















        