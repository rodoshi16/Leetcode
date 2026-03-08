class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #only start a seq if n-1 not in s
        # use a set to get rid of duplicates 
        # keep growing the length of the seq for each n 

        m = 0 
        s = set(nums)


        for n in s:
            if (n-1) not in s:
                l = 0 
                #grow a sq 
                while (n+l) in s:
                    l += 1 
                
                m = max(l, m)
        return m 
        