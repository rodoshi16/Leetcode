class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #input: nums
        #output: product of all nums except for nums[i]
        # 0(n), 0(1)

        # res = []
        # for i in range(len(nums)):
        #     p = 1 
        #     for j in range(len(nums)):
        #          j != i:
        #             p *= nums[j]
        #     res.append(p)
        # return res
    

        post = [1]
        pre = [1]
        res = []

        prev = nums[0]
        for i in range(1,len(nums)):
            pre.append(prev)
            prev *= nums[i]

        curr = nums[len(nums)-1]
        for i in range(len(nums) -2,-1, -1):
            post.append(curr)
            curr *= nums[i]

        post = post[::-1]

        for i in range(len(nums)):
            res.append(pre[i] * post[i])

        return res


