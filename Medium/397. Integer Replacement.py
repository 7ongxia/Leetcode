class Solution:
    def recursion(self, n: int) -> int:
        if n == 1:
            return 0

        if n in self.dp:
            return self.dp[n]

        match n % 2:
            case 0:
                self.dp[n] = self.recursion(n // 2) + 1
            case _:
                self.dp[n] = min(self.recursion(n - 1),
                                 self.recursion(n + 1)) + 1

        return self.dp[n]

    def integerReplacement(self, n: int) -> int:
        self.dp = {}
        return self.recursion(n)
