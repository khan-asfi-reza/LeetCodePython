class Solution:
    def myAtoi(self, s: str) -> int:
        hashMap = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "0": 0,
            "+": +1,
            "-": -1
        }

        summation = 0
        sign = 1
        number_start_point = None
        number_started = False

        for key, char in enumerate(s):
            if char == "+" or char == "-":
                if number_start_point is not None and key > number_start_point:
                    break
                elif key < len(s) - 1 and (s[key + 1] == "+" or s[key + 1] == "-" or s[key+1] == " "):
                    break
                else:
                    sign = hashMap[char]

            elif char == " ":
                if number_start_point is not None and key > number_start_point:
                    break

            elif char in hashMap:
                summation = summation * 10 + hashMap[char]
                number_start_point = key if not number_started else number_start_point
                number_started = True

            else:
                break

        summation *= sign

        if -2147483648 > summation:
            return -2147483648

        elif summation > 2147483647:
            return 2147483647

        return summation

