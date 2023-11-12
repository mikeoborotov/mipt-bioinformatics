# find the minimum number of coins needed to make change
def change_problem(amount, coins):
    # an array of min number of coins needed (for amounts from 0 to provided amount)
    min_coins_needed = [float('inf')] * (amount + 1)
    
    min_coins_needed[0] = 0 # 0 if the amount is 0
    
    # run through all amounts
    for coin in coins:
        # run through each amount from coin to amount
        for i in range(coin, amount + 1):
            min_coins_needed[i] = min(min_coins_needed[i], min_coins_needed[i - coin] + 1)
    
    # return result
    return min_coins_needed[amount]


if __name__ == "__main__":
    # read the dataset from file
    with open("dataset.txt", "r") as file:
        lines = file.readlines()
        amount = int(lines[0].strip())
        coins = list(map(int, lines[1].strip().split(',')))

    print(change_problem(amount, coins))