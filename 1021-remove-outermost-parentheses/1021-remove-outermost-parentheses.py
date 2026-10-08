class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans=""
        count =0
        for x in s:
            if x=="(":
                if count >0:
                    ans += x
                count += 1
            else:
                count -= 1
                if count > 0:
                    ans += x
        return ans
