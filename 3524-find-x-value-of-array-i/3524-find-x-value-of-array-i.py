class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k
        for num in nums:
            x = num % k
            new = [0] * k
            new[x] += 1
            for r in range(k):
                new[(r * x) % k] += dp[r]
            dp = new
            for r in range(k):
                ans[r] += dp[r]
        return ans