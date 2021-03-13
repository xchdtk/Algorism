n = int(input())  # 26
a = n
count = 0
while True:
    print(n)
    one   = n//10
    two   = n%10  
    total = one + two  
    if total < 10:
        total = str(total)[0] 
    else:
        total = str(total)[1] 
    n = str(two) + total   
    n = int(n)
    count = count + 1
    if a == n:
        break
print("***********************")
print(count)       
    
        
    