class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a=[nums[0]]
        b=[nums[1]]
        for i in range(2,len(nums)):
            x=a[len(a)-1]
            y=b[len(b)-1]
            if x>y:
                a.append(nums[i])
            else:
                b.append(nums[i])
        return a+b