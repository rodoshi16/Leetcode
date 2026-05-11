class NumArray:
    n: List[int]

    def __init__(self, nums: List[int]):
        self.n = nums
        

    def sumRange(self, left: int, right: int) -> int:
        sum = 0 
        for i in range(left, right+1):
            sum += self.n[i]
        return sum

        
        

    

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

