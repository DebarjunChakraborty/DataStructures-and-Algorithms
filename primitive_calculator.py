def compute_operations(n):
    dp = [0] * (n + 1)
    prev = [0] * (n + 1)
    dp[1] = 0
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        prev[i] = i - 1
        if i % 2 == 0:
            if dp[i // 2] + 1 < dp[i]:
                dp[i] = dp[i // 2] + 1
                prev[i] = i // 2
        if i % 3 == 0:
            if dp[i // 3] + 1 < dp[i]:
                dp[i] = dp[i // 3] + 1
                prev[i] = i // 3
    sequence = []
    while n > 0:
        sequence.append(n)
        n = prev[n]
    return sequence[::-1]
if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
