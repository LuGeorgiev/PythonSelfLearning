input_line = input().lower().split(' ')

occ_dict = {}
for word in input_line:
    occ_dict[word] = input_line.count(word)
for key, value in occ_dict.items():
    if value % 2 == 1:
        print(f'{key}', end=' ')

