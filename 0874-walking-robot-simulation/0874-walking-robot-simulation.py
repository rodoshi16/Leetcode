class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        #(0,0), facing north
        #edge: obstacle at (0,0): wait to move off

        pos = (0,0)
        x = pos[0]
        y = pos[1]
        curr = 0
        max_d = 0 

        d = set()

        for ele in obstacles:
            d.add(tuple(ele))

        directions = [(0,1), (1,0),(0,-1),(-1,0)] 

        for i in range(len(commands)):
            if commands[i] == -1:
                curr = (curr + 1) % 4

            
            elif commands[i] == -2:
                curr = (curr - 1) % 4
            
            else:
                (a,b) = directions[curr]
                for _ in range(commands[i]):
                    if (x+a,y+b) in d:
                        break
                    
                    x += a
                    y += b

            max_d = max(max_d, (x**2 + y**2))
        
        return max_d