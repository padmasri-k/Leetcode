class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        c=bin(a)
        d=bin(b)
        e=c.count('1')
        f=d.count('1')
        if e>=f:
            return e*f
        else:
            return f//e