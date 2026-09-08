class Solution:
    def countCommas(self, n: int) -> int:
        count = []
        result = 0
        for i in range(1,n+1):
          digits = len(str(i))  
          if digits < 4:
                continue
          result = result + (digits-1)//3
        return result        

        
            



            

        