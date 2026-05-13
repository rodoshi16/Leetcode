class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1}
        n = 0
        curr = 0 
        for i in range(len(nums)):
            curr += nums[i]
            c = curr - k
            if c in d:
                n += d[c]
            if curr not in d: 
                d[curr] = 1
            else:
                d[curr] += 1
        return n 


        #[1,1,1]
        #[0,1,2,2,3], 2
        # 1:1, 2:1, 2:1, 3:1
    
        # c = 1, n = 2  
        # 1: 1, 2:1, 3:1

        #[1,2,3]
        #[0, 1, 3, 6]
        # n = 0, c = 2
        # 1: 1, 3:1, 6:1

        #[1,1,1]
        #[0, 1, 2, 3]
        
        [0,0,2]

        


           