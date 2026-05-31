class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [nums[0], -nums[0]]
        c = 0 

        if len(nums) == 1:
            if nums[0] == 0:
                return 2 
            elif nums[0] == target or -nums[0] == target:
                return 1 
            else:
                return 0 

        for i in range(1, len(nums)):
            s = []
            for ele in dp:
                s.append(ele + nums[i])
                s.append(ele - nums[i])
            
            dp = s

            if i == len(nums) -1:
                for ele in s:
                    if ele == target:
                        c += 1 
        
        return c 

        




            



        
        # dp = [nums[0], -nums[0]]

        # if len(nums) == 1:
        #     if nums[0] == 0:
        #         return 2
        #     elif nums[0] == target or -nums[0] == target:
        #         return 1
        #     else:
        #         return 0



        # c = 0 

        # for i in range(1, len(nums)):
        #     s = []
        #     for ele in dp:
        #         s.append(ele + nums[i])
        #         s.append(ele - nums[i])
        
        #     dp = s 
        

        #     if i == len(nums) -1:
        #         for ele in dp:
        #             if ele == target:
        #                 c += 1 

        # return c
                
            

        