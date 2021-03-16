
n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
check = int(input())
check_list = list(map(int, input().split()))

right = []

for check in check_list:
    status = False
    start = 0
    end   = len(n_list) - 1
    while start <= end:
        midle = (start + end) // 2
        if n_list[midle] == check:
            print(1, end=' ')
            status = True
            break

        elif n_list[midle] > check:
            end = midle-1

        else:
            start = midle+1
    if not status:
        print(0, end=' ')




    