# 방문길이

def solution(dirs):
    count = 0
    new_1 = (0,0)
    visited = []
    str_dict = {"U":(0,1), "D":(0,-1) ,  "R":(1,0) ,  "L": (-1,0)}
    for index in dirs:
        str_dict_delta = str_dict[index]
        new = (new_1[0]+str_dict_delta[0] ,  new_1[1]+str_dict_delta[1])
        if  (5 < abs(new[0])) or (5 < abs(new[1])):
            continue
        if (new_1,new) not in visited:
            visited.append((new_1,new))
            visited.append((new,new_1))
            count = count + 1
        new_1 = new
    return count      
