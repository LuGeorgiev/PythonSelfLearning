target_key = input()
target_value = input()
lines = int(input())
data_dict = {}

for num in range(0, lines):
    tokens_list = input().split(' => ')
    key = tokens_list[0]
    value_list = tokens_list[1].split(';')
    data_dict[key] = value_list

for k, v in data_dict.items():
    if target_key in k:
        print(f'{k}:')
        for el in v:
            if target_value in el:
                print(f'-{el}')
