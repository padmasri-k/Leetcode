class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sum=0
        n=len(nums)
        for i in range(len(nums)):
            if n%(i+1)==0:
                p=nums[i]*nums[i]
                sum+=p
        return sum
