class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        dp = [0 for i in range(len(s) + 1)]

        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1

        for i in range(2, len(s) + 1):
            # one step jump
            if int(s[i - 1]) != 0:
                dp[i] += dp[i - 1]
            # two step jump
            if 10 <= int(s[i - 2 : i]) <= 26:
                    dp[i] += dp[i - 2]
        
        print(dp)
        
        return dp[len(s)]
                