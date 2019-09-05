data_list = input().split(' -> ')
names_dict = {}
while not data_list[0] == 'end':
    name = data_list[0]
    tokens = data_list[1].split(', ')
    if tokens[0].isdigit():
        if name not in names_dict.keys():
            names_dict[name] = []
        else:
            names_dict[name].extend(tokens)
    else:
        if tokens[0] in names_dict.keys():
            if name not in names_dict.keys():
                names_dict[name] = []
            names_dict[name].extend(names_dict[tokens[0]])
            
    data_list = input().split(' -> ')
