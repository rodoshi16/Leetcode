class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #turn n+1

        # take ele and mark its position negative 
        # work with abs and ignore > n 
        # scan to find first missing positive 


        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums) + 1 
        

        for i in range(len(nums)):
            val = abs(nums[i])
            if val <= len(nums) and nums[val-1] > 0: 
                    nums[val-1] = - nums[val-1]
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1
        
        return len(nums)+1

           


        