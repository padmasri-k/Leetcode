class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        count=0
        for i in range(len(nums)):
            a=nums[i]
            m=nums[i]
            for j in range(i,len(nums)):
                a &= nums[j]
                m=min(m,nums[j])
                if a==m:
                    count += 1
        return count