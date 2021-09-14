# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
# 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

# re.sub
# 예를 들어
# re.sub('aple', 'apple', text) -> text중에서 문자열 aple를 apple로 치환

import re
def solution(new_id):
    result = ''
    # 1단계, 2단계
    result = re.sub('[^a-z\d\-\_\.]', '', new_id.lower())

    # 3단계
    result = re.sub('\.\.+', '.', result)

    # 4단계
    result = re.sub('^\.|\.$', '', result)

    # 5단계
    if not result:
        result = "a"

    # 6단계
    if len(result) >= 16:
        result = re.sub('\.$', '', result[0:15])
    
    # 7단계
    if len(result) <= 2:
        len_string = 3 - len(result)
        for number in range(len_string):
            result += result[-1]
    
    return result


new_id = "=.="
print(solution(new_id))
