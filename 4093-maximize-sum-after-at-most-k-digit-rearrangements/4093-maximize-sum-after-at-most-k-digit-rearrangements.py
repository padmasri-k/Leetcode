class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        b=nums.copy()
        a=[]
        for i in nums:
            s=int("".join(sorted(str(i),reverse=True)))
            a.append(s-i)
        a.sort(reverse=True)
        return sum(nums)+sum(a[:k])