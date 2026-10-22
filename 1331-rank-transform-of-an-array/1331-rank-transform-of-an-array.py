class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        a=sorted(set(arr))
        d={}
        for i in range(len(a)):
            d[a[i]]=i+1
        res=[]
        for i in arr:
            res.append(d[i])
        return res
