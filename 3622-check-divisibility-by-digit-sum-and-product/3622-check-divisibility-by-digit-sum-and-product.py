class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x=n
        s=0
        p=1
        while n>0:
            r=n%10
            s+=r
            p*=r
            n=n//10
        if x%(s+p)==0:
            return True
        else:
            return False

        
            