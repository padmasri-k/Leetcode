class Solution:
    def reverseDegree(self, s: str) -> int:
        sum=0
        for i in range(len(s)):
            j=123-ord(s[i])
            sum += j*(i+1)
        return sum
        


