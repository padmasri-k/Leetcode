class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        x=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if j==i+1 and nums[i]^nums[j] == 0:
                    x += 1
        return x
          