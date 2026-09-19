class Solution:
    def primePalindrome(self, n: int) -> int:
        def isPrime(x):
            if x < 2:
                return False
            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 1
            return True
        if 8 <= n <= 11:
            return 11
        for x in range(1, 100000):
            s = str(x)
            # Create an odd-length palindrome
            p = int(s + s[-2::-1])
            if p >= n and isPrime(p):
                return p