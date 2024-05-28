MOD = 10**9 + 7

def count_numbers_with_at_most_k_distinct_digits(k, m, n, l, r):
    def count_numbers_up_to(n, K):
        # DP array to store the count of numbers up to i with at most j distinct digits
        dp = [[0] * (K + 1) for _ in range(len(n) + 1)]
        dp[0][0] = 1

        for i in range(1, len(n) + 1):
            for j in range(K + 1):
                for digit in range(1 if i == 1 else 0, 10):
                    if digit <= int(n[i - 1]):
                        dp[i][j] += dp[i - 1][j - (digit < int(n[i - 1]))]
                        dp[i][j] %= MOD

                if j > 0:
                    dp[i][j] += dp[i - 1][j - 1] * (int(n[i - 1]) - 1)
                    dp[i][j] %= MOD

        return sum(dp[-1][:K + 1]) % MOD

    return (count_numbers_up_to(r, k) - count_numbers_up_to(l, k - 1)) % MOD

# Read input
k = int(input().strip())
m = int(input().strip())
n = int(input().strip())
l = input().strip()
r = input().strip()

# Example usage:
print("Count of numbers between l and r with at most k distinct digits:",
      count_numbers_with_at_most_k_distinct_digits(k, m, n, l, r))
    