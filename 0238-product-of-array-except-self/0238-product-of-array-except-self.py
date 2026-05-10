class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []

        prev = 1
        for i in range(len(nums)):
            res.append(prev)
            prev *= nums[i]

        curr = 1
        for i in range(len(nums) -1,-1, -1):
            res[i] = res[i] * curr
            curr *= nums[i]

        return res