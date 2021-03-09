def tree_cutting(n, m, tree_list):
    tree_list.sort() # 이분 탐색은 오름차순 정렬
    start = 0
    end   = max(tree_list)
    
    while start <= end:
        mid  = (start + end) // 2

        tree_count = 0
        for tree in tree_list:
            if tree > mid:
                tree_count += tree - mid

        if tree_count >= m:
            start = mid + 1
        else:
            end = mid - 1
    return end  

n,m       = map(int,input().split())
tree_list = list(map(int, input().split())) 
print(tree_cutting(n, m, tree_list))




