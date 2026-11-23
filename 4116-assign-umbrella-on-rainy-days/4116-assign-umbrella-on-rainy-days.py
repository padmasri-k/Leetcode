class Solution:
    def assignUmbrella(self, rain: list[int]) -> list[str]:
        n=len(rain)
        ans=[]
        alice=0
        bob=0
        for i in range(n):
            a=rain[i]==1 and i<n-1 and rain[i+1]==1
            b=rain[i]==1
            if a and b:
                if alice<=bob:
                    ans.append("Alice")
                    alice+=1
                else:
                    ans.append("Bob")
                    bob+=1
            elif a:
                 ans.append("Alice")
                 alice+=1
            elif b:
                ans.append("Bob")
                bob+=1
            else:
                ans.append("None")
        return ans
            
           
            
                