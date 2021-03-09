words      = input().upper()
set_words  = list(set(words))
count_list = []

for word in set_words:
    cnt        = words.count(word)
    count_list.append(cnt)
print(count_list)
print(set_words)
if count_list.count(max(count_list)) > 1:
    print("?")
else:
    index = count_list.index(max(count_list))
    
    print(set_words[index])
    