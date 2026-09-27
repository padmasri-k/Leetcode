class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        ans=[]
        nums2=set(nums2)
        for i in nums1:
            if i in nums2:
                ans.append(i)
        if len(ans)==0:
            return -1
        return min(ans)