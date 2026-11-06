class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        s=int(str(nums[0])+str(nums[1]))
        for i in range(2,len(nums),2):
            a=int(str(nums[i])+str(nums[i+1]))
            s=min(s,a)
        return s
        
            