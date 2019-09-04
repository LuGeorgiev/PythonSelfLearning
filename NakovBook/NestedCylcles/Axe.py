def print_top(num_int, width_int):
    front_dashes = ('-' * (num_int * 3))
    for i in range (0, num):
        back_dashes = ('-' * (width - len(front_dashes) - 2 - i))
        mid_dashes = ('-' * i)
        print(f'{front_dashes}*{mid_dashes}*{back_dashes}')


def print_handle(num_int, height_int):
    front_starts = ('*' * (num_int * 3 + 1))
    mid_dashes = ('-' * (num_int - 1))
    last_dashes = ('-' * ((num_int * 5) - len(front_starts) - len(mid_dashes) - 1))
    for i in range(height_int):
        print(f'{front_starts}{mid_dashes}*{last_dashes}')


def print_blade(num_int, height_int):
    for i in range(0, height_int):
        front_dashes = ('-' * (num_int * 3 - i))
        mid_dashes = ('-' * (num_int - 1 + (2 * i)))
        last_dashes = ('-' * ((num_int * 5) - len(front_dashes) - len(mid_dashes) - 2))
        print(f'{front_dashes}*{mid_dashes}*{last_dashes}')
    return len(front_dashes), len(mid_dashes)


num = int(input())
width = num * 5
blade_hand_height = num // 2

print_top(num, width)
print_handle(num, blade_hand_height)
if num > 2:
    if num == 3:
        dash_qty, starts_qty = print_blade(num, blade_hand_height)
    else:
        dash_qty, starts_qty = print_blade(num, blade_hand_height - 1)
else:
    dash_qty = 7
    starts_qty = -1
dashes = ('-' * (dash_qty - 1))
starts = ('*' * (starts_qty + 4))
last_lashes =('-' * (width - dash_qty - starts_qty - 3))
print(f'{dashes}{starts}{last_lashes}')

