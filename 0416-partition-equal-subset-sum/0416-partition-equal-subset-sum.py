class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        if n == 1 or total % 2 == 1:
            return False
        
        target = total // 2

        r = set()
        r.add(0)
    
        for i in range(len(nums)):
            if nums[i] == target:
                return True 
            
            s = set()
            for ele in r:
                n = nums[i] + ele
                s.add(n)
                if n == target:
                    return True
            for ele in s:
                r.add(ele)
            
        return False
        



            

            



        return False
        