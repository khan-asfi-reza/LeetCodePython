# Solution 1
def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    res = ['' for _ in range(numRows)]
    row = 0
    d = -1

    for val in s:
        res[row] += val
        if row == 0 or row == numRows - 1:
            d *= -1

        row += d

    return "".join([each for each in res])


# Solution 2
def convert_2(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    res = ""
    jump = 2 * numRows - 2
    for i in range(numRows):
        for j in range(i, len(s), jump):
            res += s[j]
            k = j + jump - 2 * i
            if i != 0 and i != numRows - 1 and k < len(s):
                res += s[k]

    return res

