data_list = input().split(' = ')
names_dict = {}

while data_list[0] != "end":
    if data_list[1].isdigit():
        names_dict[data_list[0]] = int(data_list[1])
    else:
        if data_list[1] in names_dict.keys():
            names_dict[data_list[0]] = names_dict[data_list[1]]
        else:
            continue
    data_list = input().split(' = ')

for k, v in names_dict.items():
    print(f'{k} === {v}')
