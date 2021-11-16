def solution(clothes):
    dict_clothes = {}
    answer = 1
    for index in range(len(clothes)):
        if clothes[index][1] in dict_clothes:
            dict_clothes[clothes[index][1]].append(clothes[index][0])
        else:
            dict_clothes[clothes[index][1]] = [clothes[index][0]]
    for key in dict_clothes.keys():
        answer += answer * len(dict_clothes[key])
    return answer - 1


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"], ["jean", " Pants"]]
print(solution(clothes))
