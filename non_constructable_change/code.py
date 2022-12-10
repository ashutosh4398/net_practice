from typing import List

def nonConstructibleChange(coins: List[int]) -> int:
    # Write your code here.
    # sorting the list of coins
    coins.sort()
    cumulative_sum_till_current_coin: int = 0
    n: int = len(coins)
    for i in range(len(coins)):
        current_coin = coins[i]
        # avoiding index error: i < n - 1
        if (cumulative_sum_till_current_coin + 1) < current_coin:
            return cumulative_sum_till_current_coin + 1
        cumulative_sum_till_current_coin += current_coin

    return cumulative_sum_till_current_coin + 1


print(nonConstructibleChange([87]))
print(nonConstructibleChange([1,2,5]))
print(nonConstructibleChange([5,7,1,1,2,3,22]))