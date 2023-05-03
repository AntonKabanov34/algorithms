import time

start_time = time.time()

anagram = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagram_dict = {}

out = []
for i in anagram:
    sort_leter = ''.join(sorted(i.lower()))
    if sort_leter in anagram_dict:
        anagram_dict[sort_leter].append(i)
    else:
        anagram_dict[sort_leter] = [i]

for k, value in anagram_dict.items():
    if len(value) >= 1:
        out.append(value)
    else:
        pass
end_time = time.time()

all_time = end_time - start_time

print(out)
print(f'Время выполнения кода: {all_time} секунд')
