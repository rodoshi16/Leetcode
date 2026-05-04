class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #input: nums-> list of integers
        # move all zeros at the end while maintaing order
        # brute: scan and if zero -> pop and append zero at end 

        # i = 0 
        # while i < len(nums):
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         nums.append(0)
        #     i += 1 
        

        #modifying loop while iterating
        #edge cases: [0, 0, 8, 1, 2] (move to the next index but next index is pushed down)
        # pop shifts everything left but index still moves right

        left = 0 
        right = len(nums) - 1 

        left = 0 
        right = 1 

        while right < len(nums):
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right += 1 
            elif nums[left] == 0 and nums[right] == 0:
                right += 1 
            else: 
                left += 1 
                right += 1 


        

        
        
        


        