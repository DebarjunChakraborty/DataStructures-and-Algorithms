def change(money):
    denominations = [10, 5, 1]
    num_coins = 0
    for coin in denominations:
        num_coins += money // coin
        money %= coin
    return num_coins
if __name__ == '__main__':
    m = int(input())
    print(change(m))