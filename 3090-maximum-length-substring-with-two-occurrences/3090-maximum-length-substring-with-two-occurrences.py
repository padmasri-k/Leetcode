class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        ans = 0

        for i in range(len(s)):
            for j in range(i, len(s)):

                x = s[i:j+1]

                if all(x.count(c) <= 2 for c in x):
                    if len(x) > ans:
                        ans = len(x)

        return ans