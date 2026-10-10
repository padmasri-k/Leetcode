class Solution:
    def minChanges(self, n: int, k: int) -> int:
        count = 0
        while n > 0 or k > 0:
            if n % 2 == 0 and k % 2 == 1:
                return -1
            if n % 2 == 1 and k % 2 == 0:
                count += 1
            n //= 2
            k //= 2
        return count