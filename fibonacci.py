# Dynamic Recursive
def fibonacci(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]

    if n == 1 or n == 2:
        result = 1

    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)

    memo[n] = result

    return result


# Dynamic Bottom Up
def fibonacci_btm(n):
    if n == 1 or n == 2:
        return 1

    else:
        lst = [1, 1]
        for i in range(2, n):
            lst.append(lst[i - 1] + lst[i - 2])

        return lst[n - 1]



