class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        last_value = 0
        number = 0

        for each in s:
            if hashmap[each] <= last_value:
                number += last_value

            else:
                number -= last_value

            last_value = hashmap[each]

        number += last_value

        return number



