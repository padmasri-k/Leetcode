class Solution:
    def check(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            if nums[i:]+nums[:i]==sorted(nums):
                return True
         
        return False