with open('my-file.txt', 'r') as file:
    row_text = file.readlines()
    odd_rows_text = [row_text[index] for index in range(len(row_text)) if index % 2 == 1]

with open('output-odd.txt', 'a') as output:
    output.write(''.join(odd_rows_text))