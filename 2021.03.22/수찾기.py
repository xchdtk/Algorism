n = int(input())
n_list = list(map(int,input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int,input().split()))


for number in m_list:
    start = 0
    end   = len(n_list) - 1
    status = False
    while start <= end:

        mid = (start + end) //2
    
        if n_list[mid] == number:
            status = True
            break
        elif n_list[mid] < number:
            start = mid+1

        else:
            end = mid - 1

    if status:
        print(1)
    else:
        print(0)
    