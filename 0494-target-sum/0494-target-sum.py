class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # time: 0(n*sum(nums)) - the max number of keys stored in the dict is between -sum(nums) and sum(nums)
        # space: 0(sum(nums))

        if len(nums) == 1:
            if nums[0] == 0:
                return 2 
            elif nums[0] == target or -nums[0] == target:
                return 1 
            else:
                return 0 

        if nums[0] == 0:
            dp = {0: 2}
        else: 
            dp = {nums[0]:1, -nums[0]: 1}


        for i in range(1, len(nums)):
            s = {}
            for ele in dp:
                a = ele + nums[i]
                b = ele - nums[i]
                s[a] = s.get(a, 0) + dp[ele]
                s[b] = s.get(b, 0) + dp[ele]
            
            dp = s
        
        if target in dp:
            return dp[target]
        else:
            return 0
