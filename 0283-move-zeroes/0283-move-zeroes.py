class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #naive: scan until zero, pop and append 
        # 2 pointer 
        
        # [0,1,0,3,12]
        #everything on left -> non zero

        left = 0 
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left +=1 














      