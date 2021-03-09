n = int(input())

for number in range(n):
    h, w , n  = list(map(int, input().split()))
    print(h, w, n)
    room = [1,2,3]
    ho    = room[2] // room[0] + 1
    layer = room[2] % room[0]

    if layer == 0:
        ho = ho - 1
        layer = room[0] 

    print(layer * 100 + ho)

    
    