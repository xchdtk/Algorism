import sys

number = int(sys.stdin.readline())
stack_1 = list()
for i in range(number):
    x = int(sys.stdin.readline())
    if x:
        stack_1.append(x)
        continue
    stack_1.pop()
print(sum(stack_1))