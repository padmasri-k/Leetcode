class Solution:
    def maxProduct(self, n: int) -> int:
       s=str(n)
       s=sorted(s)
       return (int(s[-1])*int(s[-2]))