class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # same amount of 0 and 1 
        # [0,1]
        # [0,1,0], [0, 1, 1]
        # [0,1,1,1,1,1,0,0,0], [0, 1, 2, 3, 4, 5, 5, 5, 5]
        # sum not changing: seq of 0s
        # sum changing: seq of 1s

        # 0: 1, -1: 0, 
        #

        #subarrays
        currSum = 0 
        d = {0: -1}
        n = 0 
        m = 0
        for i in range(len(nums)):
            if nums[i] == 1: 
                currSum += nums[i]
            else:
                currSum -= 1
            if currSum not in d:
                d[currSum] = i 
            else:
                m = max(m, i - d[currSum])
    
        return m 

            
            
            
        

        