class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[""]
        for i in range(2*n):
            temp=[]
            for s in ans:
                if s.count("(") < n:
                    temp.append(s+"(")
                if s.count(")")<s.count("("):
                    temp.append(s+")")
            ans=temp
        return ans
