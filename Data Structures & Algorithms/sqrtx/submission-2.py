class Solution:
    def mySqrt(self, x: int) -> int:
        # 9 ... 9/2 = 4 (0,4) ...4..4/2 = 2 (2,4)
        # 2+4/2 = 3 

        # 13 ... 13/2 = 6 (0,6) ... (0+6)/2 = 3 3*3 = 9 < 13 
        # (3,6)/2 = 4, 16 > 13....(3,4) = 3

        start = 0  #1 2
        end = x #2 1
        root = 0 #1

        while start <= end:
            m = start + (end-start) // 2  # 0 1
            square = m * m #0 1 
            
            
            if square > x: 
                end = m -1  #1 
            elif square < x: 
                start = m +1  # 1 2
                root = m #1
            else:
                return m

        return root 


            
            



            


