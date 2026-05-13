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