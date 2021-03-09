import math

n=int(input())      # 테스트케이스 5번을 돌릴 것이다.

for i in range(n):
    sum_1=0
    count=0
    a=list(map(int,input().split()))
    for j in range(1,len(a)):   # 합계
        sum_1+=a[j]
    sum_1=sum_1/a[0]
    for p in range(1,len(a)):
        if sum_1<a[p]:
            count=count+1   
    print("%.3f"%(count*100/a[0])+"%")


# 5개가 주어질때 
 