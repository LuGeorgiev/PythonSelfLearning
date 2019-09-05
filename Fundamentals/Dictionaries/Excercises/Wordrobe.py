n = int(input())
wardrobe_dict = {}
for i in range(n):
    data_list = input().split(' -> ')
    color = data_list[0]
    clothes_list = data_list[1].split(',')
    if color not in wardrobe_dict.keys():
        wardrobe_dict[color] = []
    wardrobe_dict[color].extend(clothes_list)

items_count_dict = {}
for col, cloth_list in wardrobe_dict.items():
    items_count_dict[col] = {c: cloth_list.count(c) for c in cloth_list}

tokens = input().split()
target_col = tokens[0]
target_garment = ' '.join(tokens[1:])

for color, kvp in items_count_dict.items():
    print(f'{color} clothes: ')
    for garment, garment_count in kvp.items():
        if target_col == color and target_garment == garment:
            print(f'* {garment} - {garment_count} (found)')
        else:
            print(f'* {garment} - {garment_count}')
