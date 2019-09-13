with open('odd.txt', 'r') as file:
    odd_num = file.readlines()

with open('even.txt', 'r') as file:
    even_num = file.readlines()

merged = list(zip(odd_num, even_num))
with open('merged-output.txt', 'a') as file:
    for el in merged:
        file.write(el[0])
        file.write(el[1])

