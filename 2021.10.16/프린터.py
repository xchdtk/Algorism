from collections import deque

def max_target(documents):
    target = documents[0]
    for index in range(1, len(documents)):
        if target[1] < documents[index][1]:
            target = documents[index]

    return target
        
def solution(priorities, location):
    documents = deque([index, priorities[index]] for index in range(len(priorities)))
    count = 0
    while documents:
        max_documents = max_target(documents)
        first_document = documents.popleft()
        
        if max_documents == first_document:
            count += 1
            if first_document[0] != location:
                continue
            return count
            
        documents.append(first_document)


priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))


