# Write a program that writes out how to pay a given amount of money (in eurocent) with a minimum number of coins (using coins of 2 or 1 euro, or 50, 20, 10, 5, 2, or 1 eurocent).

# Input
# The input consists of a single line containing an integer: the amount of money to be paid (in eurocent).

# Output
# On a separate line for each type of coin, the number of coins necessary to pay the requested amount.

# Example
# Input:

# 589
# Output:

# 2-euros: 2
# 1-euros: 1
# 50c-euros: 1  
# 20c-euros: 1
# 10c-euros: 1
# 5c-euros: 1
# 2c-euros: 2
# 1c-euros: 0

money = int(input())

coins = [
    (200, "2-euros"),
    (100, "1-euros"),
    (50, "50c-euros"),
    (20, "20c-euros"),
    (10, "10c-euros"),
    (5, "5c-euros"),
    (2, "2c-euros"),
    (1, "1c-euros"),
]

for coin, label in coins:
    count = 0
    while money >= coin:
        money = money - coin
        count = count + 1
    print(f"{label}: {count}")
