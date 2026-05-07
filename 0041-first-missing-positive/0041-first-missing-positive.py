class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #list: unsorted 
        #output: smallest positive integer not present in nums

        #iteration to make a hashmap + iterate through hashmap 


        d = {}
        for ele in nums:
            if ele not in d:
                d[ele] = 1 
    
        for i in range(1, len(nums) + 2):
            if i not in d:
                return i 
        