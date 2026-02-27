class Solution:
    def popo(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        sqx = self.popo(x, n // 2)
        sqx *= sqx

        if n % 2 == 1:
            sqx *= x
        
        return sqx
    def myPow(self, x: float, n: int) -> float:
        ans = self.popo(x, abs(n))
        if n < 0:
            ans = 1 / ans
        return ans