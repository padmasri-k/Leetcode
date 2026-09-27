class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        ans=[]
        for i in nums:
            for j in str(i):
                ans.append(int(j))
        return ans