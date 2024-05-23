def partition3(values):
    total_sum = sum(values)
    n = len(values)
    if n < 3 or total_sum % 3 != 0:
        return 0
    target_sum = total_sum // 3
    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(1, n + 1):
        for j in range(target_sum + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= values[i - 1]:
                dp[i][j] |= dp[i - 1][j - values[i - 1]]
    if not dp[n][target_sum]:
        return 0
    remaining_sum = [target_sum] * 3
    for i in range(n, 0, -1):
        for j in range(3):
            if remaining_sum[j] >= values[i - 1] and dp[i - 1][remaining_sum[j] - values[i - 1]]:
                remaining_sum[j] -= values[i - 1]
    if sum(remaining_sum) == 0:
        return 1
    else:
        return 0
if __name__ == '__main__':
    input_n = int(input())
    input_values = list(map(int, input().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
