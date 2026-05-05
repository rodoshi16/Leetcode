from collections import deque 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       #input: nums
       #output: return the majority element

       #scan and map 
       # scan through dict and check count 

       if len(nums) == 1:
            return nums[0]

       d = {}
       for ele in nums:
            if ele not in d:
                d[ele] = 1
            else:
                d[ele] += 1 
                if d[ele] > len(nums)/2:
                    return ele
        
