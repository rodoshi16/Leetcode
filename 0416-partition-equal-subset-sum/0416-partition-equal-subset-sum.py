class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if len(nums) == 1 or total % 2 == 1:
            return False 
        
        target = total // 2 

        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            if nums[i] == target:
                return True

            s = set()
            for ele in dp:
                n = nums[i] + ele
                if n == target:
                    return True
                s.add(n)
            
            for ele in s:
                dp.add(ele)
        
        return False
            




        