class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        #each element will be pushed and popped only once
        # 

        res = [0] * len(heights)
        if not heights:
            return []

        stack = [heights[-1]]
        i = len(heights) - 2

        while i >= 0:
            count = 0

            while stack and heights[i] > stack[-1]:
                stack.pop()
                count += 1
            

            if stack:
                count += 1
            
            res[i] = count
            stack.append(heights[i])
            i -= 1
    
        
        return res








