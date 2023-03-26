def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort(reverse=False)
    waiting_time = 0
    result = 0
    for i in queries:
        result += waiting_time
        waiting_time += i
    return result



print(minimumWaitingTime([3, 2, 1, 2, 6]))
print(minimumWaitingTime([1,4,5]))