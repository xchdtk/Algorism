expression = input().split('-')
result = 0 

for i in map(int,expression[0].split('+')):
    result += i

for i in expression[1:]:
    for j in i.split("+"):
        result -= int(j)      
print(result)