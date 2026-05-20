class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1 or sum(nums) % 2 == 1:
            return False 
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums)):
            if nums[i] == target:
                return True
            s = set()
            for ele in dp:
                e = nums[i] + ele
                s.add(e)
                if e == target:
                    return True
            for ele in s:
                dp.add(ele)
        
        return False
    
        
        