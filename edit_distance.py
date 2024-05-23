def edit_distance(first_string, second_string):
    n = len(first_string)
    m = len(second_string)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                dp[i][j] = j 
            elif j == 0:
                dp[i][0] = i
            elif first_string[i - 1] == second_string[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],    
                                   dp[i][j - 1],   
                                   dp[i - 1][j - 1]) 
    return dp[n][m]
if __name__ == "__main__":
    print(edit_distance(input(), input()))