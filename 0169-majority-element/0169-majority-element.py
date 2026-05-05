from collections import deque 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #         return nums[0]

        # d = {}
        # for ele in nums:
        #         if ele not in d:
        #             d[ele] = 1
        #         else:
        #             d[ele] += 1 
        #             if d[ele] > len(nums)/2:
        #                 return ele

        candidate = None
        count = 0 

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1 
            else:
                count -=1 
        return candidate 