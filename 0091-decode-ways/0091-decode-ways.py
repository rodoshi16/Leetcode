class Solution:
    def numDecodings(self, s: str) -> int:
        #input: string of numbers
        #output: number of ways to decode this

        #at most 2 groups
        # 0 is invalid

        # choices: take it individually or together with another

        #any intger except for zero can be taken

        num = 0 
        memo = {}

        def ways(s):
            num = 0
            if s == "0":
                return 0
            
            #you've reached the end successfully without returning 0
            elif s == "":
                return 1


            one = s[0]
            if one != "0":
                if s[1:] not in memo:
                    memo[s[1:]] = ways(s[1:])
                num += memo[s[1:]]

        
            two = s[0:2]
            if 10 <= int(two) <= 26:
                if s[2:] not in memo:
                    memo[s[2:]] = ways(s[2:])
                num += memo[s[2:]]
             
            return num

        return ways(s)


    
        
                  

        