def print_top(line_int):
    upper = ('^' * (line_int//2))
    lower = ('_' * (line_int*2 - (2*len(upper)+4)))
    return f'/{upper}\\{lower}/{upper}\\'


def print_bottom(line_int):
    lower = ('_' * (line_int//2))
    upper = (' ' * (line_int*2 - (2*len(lower)+4)))
    return f'\\{lower}/{upper}\\{lower}/'


def print_last_body(line_int):
    line_len = line_int * 2
    draw_space = line_int * 2 - 2
    tilds = line_int // 2
    underline_qty = line_len - 4 - (2 * tilds)
    space_qty = (draw_space - underline_qty) // 2
    space = (' ' * space_qty)
    underline = ('_' * underline_qty)
    return f'|{space}{underline}{space}|'


lines = int(input())
if lines <= 4:
    lines_in_Body = lines - 2
else:
    lines_in_Body = lines - 3
spaces = (' ' * (lines * 2 - 2))
print(print_top(lines))
for r in range(lines_in_Body):
    print(f'|{spaces}|')
if lines > 4:
    print(print_last_body(lines))
print(print_bottom(lines))




