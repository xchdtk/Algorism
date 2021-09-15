def solution1(s):
    pass
    stack = ""
    result = ""
    for character in s:
        stack += character
        if stack == "0" or stack == "zero":
            result += "0"
            stack = ""
            continue

        if stack == "1" or stack == "one":
            result += "1"
            stack = ""
            continue

        if stack == "2" or stack == "two":
            result += "2"
            stack = ""
            continue

        if stack == "3" or stack == "three":
            result += "3"
            stack = ""
            continue

        if stack == "4" or stack == "four":
            result += "4"
            stack = ""
            continue

        if stack == "5" or stack == "five":
            result += "5"
            stack = ""
            continue

        if stack == "6" or stack == "six":
            result += "6"
            stack = ""
            continue

        if stack == "7" or stack == "seven":
            result += "7"
            stack = ""
            continue

        if stack == "8" or stack == "eight":
            result += "8"
            stack = ""
            continue

        if stack == "9" or stack == "nine":
            result += "9"
            stack = ""
            continue
    return int(result)


s = "123"
print(solution1(s))

# 다른 사람 풀이
num_dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
           "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
def solution2(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)

    return int(answer)


s = "123"
print(solution1(s))


