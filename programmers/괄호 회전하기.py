def solution(s):
    array = list(s)
    stack = []
    count = 0
    if len(s) % 2 != 0:
        return 0

    for index in range(len(s)-1):
        check = True
        if index:
            array.append(array.pop(0))

        for character in array:
            if character == '{' or character == '[' or character == '(':
                stack.append(character)

            else:
                if character == ']':
                    if stack and stack[-1] == '[':
                        stack.pop()
                        continue
                    else:
                        check = False
                        break

                if character == '}':
                    if stack and stack[-1] == '{':
                        stack.pop()
                        continue
                    else:
                        check = False
                        break

                if character == ')':
                    if stack and stack[-1] == '(':
                        stack.pop()
                        continue
                    else:
                        check = False
                        break
        if check:
            count += 1

    return count


s = "{"
print(solution(s))
