class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        for num in nums:
            new_subsets=[]
            for subset in ans:
                new_subsets.append(subset+[num])
            ans.extend(new_subsets)
        return ans
    