numbers_list = list(map(lambda x: float(x), input().split(' ')))


occ_dic = {num: numbers_list.count(num) for num in numbers_list}

#now is sorted by values, default is by key
for key, value in sorted(occ_dic.items(), key=lambda kvp: kvp[1], reverse=True):
    print(f'{key} -> {value} times')

