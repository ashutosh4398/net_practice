# Non-Constructible Change Problem
Given an array of positive integers representing the values of coins in your possession, write a function that returns the minimum amount of change (the minumum sum of money) that you cannot create. The given coins can have any positive integer value and aren't necessarily unique(ie you can have multiple coins of same value)


## Solution Explaination

The main trick here is to sort the coins array and for my current coin, calculate how much maximum sum I can create
Eg: coins = [1, 4, 5]

- with current coin = 1, max amount can be: 1
- with current coin = 4, max amount can be: 5

Now if I compare my previous max amount till (i-1)th coin, I can add 1 to it and say that it cannot be created since the next coin that I have is of 5
Thus we cannot create amount=2 with our current set of coins

## Mathematics

- Let cumulative amount till ith coin be C1
- if C1 + 1 < (i+1)th element: return C1+1 value as change cannot be created
- if we reach till end of array, then return sum(coins array) + 1 as minimum amount which cannot be created by our current set of coins