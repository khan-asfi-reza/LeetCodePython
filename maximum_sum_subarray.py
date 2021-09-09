# Kadane's Algorithm


def max_sum(lst):
    best = total = 0

    for each in lst:
        total = max(each, each + total)
        best = max(total, best)

    return best

