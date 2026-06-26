class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, current):
            if i == len(nums):
                res.append(current[:])
                return

            # Don't take nums[i]
            backtrack(i + 1, current)

            # Take nums[i]
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

        backtrack(0, [])
        return res
