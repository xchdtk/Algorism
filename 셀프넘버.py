self_num = set(range(1,1000000001))
generated_num = set()
for i in range (1,100001): # 33
    for j in str(i): # 3, 3
        i += int(j) 
    generated_num.add(i)
    
self_num = self_num - generated_num
for i in sorted(self_num):
    print(i)

a = []
a = list()

